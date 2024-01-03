from django.shortcuts import render
from .models import Firm, Client, Prestation, Bill
from .serialiser import FirmSerializer,  BillSerializer

from .forms import FirmForm, ClientForm, PrestaForm

from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from django.db import transaction
from django.forms import formset_factory



# Create your views here.

# class FirmView(APIView):
#     def get(self, request, format=None):
#         firm = Firm.objects.all()
#         serializer = FirmSerializer(firm, many=True) 

#         return Response(serializer.data)
    
# class PrestationsView(APIView):
#     def get(self, request, format=None):
#         prestations = Prestation.objects.all()
#         serializer = PrestationSerializer(prestations, many=True) 

#         return Response(serializer.data)
    
# class BillsView(APIView):
#     def get(self, request, format=None):
#         bills = Bill.objects.all()
#         serializer = BillSerializer(bills, many=True) 

#         return Response(serializer.data)
    
# class ClientsView(APIView):
#     def get(self, request, format=None):
#         clients = Client.objects.all()
#         serializer = ClientSerializer(clients, many=True) 

#         return Response(serializer.data)
    

#envoi des données de crezation de firm
class CreateFirm(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        form = FirmForm(request.data)

        if form.is_valid():
            firm = form.save(commit=False)
            firm.created_by = request.user
            firm.save()

            return Response({'status': 'created'})
        else:
            return Response({'status': 'errors', 'errors': form.errors})
        
#get renvoie les infos de l entreprise de l user authentifié put renvoie le form de modif
class MyFirm(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        firm = Firm.objects.get(created_by=request.user)
        serializer = FirmSerializer(firm, many=False) 

        return Response(serializer.data)
    
    def put(self, request):
        firm = Firm.objects.get(created_by=request.user)
        form = FirmForm(request.data, instance=firm)
        form.save()
        return Response({'status': 'edited'})
        

  

#renvoie les factures de l user authentifié, utilisé dans la liste des factures clients
class MyBills(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        # Trouver les firmes associées à l'utilisateur
        my_firm = Firm.objects.get(created_by=request.user)
        
        # Trouver les clients produits par cette firme
        my_clients = Client.objects.filter(produced_by=my_firm)
        
        # Trouver les factures associées à ces clients
        my_bills = Bill.objects.filter(client__in=my_clients)
        
        
        serializer = BillSerializer(my_bills, many=True)
        return Response(serializer.data)


#renvoie toutes les infos utile a la visualisation de la facture (prestataire, client, facture, presation)
class BillDetailView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, pk, format=None):
        my_firm = Firm.objects.get(created_by=request.user)
        my_clients = Client.objects.filter(produced_by=my_firm)
        bill = Bill.objects.get(pk=pk, client__in=my_clients)
        #autre methode   bill = get_object_or_404(Bill, pk=pk, client__in=my_clients)
        serializer = BillSerializer(bill) 
        return Response(serializer.data)

    
    def delete(self, request, pk):
        my_firm = Firm.objects.get(created_by=request.user)
        my_clients = Client.objects.filter(produced_by=my_firm)
        bill = Bill.objects.get(pk=pk, client__in=my_clients)
        bill.delete()

        return Response({'status': 'delete'})
    
    def put(self, request, pk):
        print("Data reçue :", request.data)  
        my_firm = Firm.objects.get(created_by=request.user)
        my_clients = Client.objects.filter(produced_by=my_firm)
        bill = Bill.objects.get(pk=pk, client__in=my_clients)
    
        serializer = BillSerializer(bill, data=request.data, partial=True)
    
        if serializer.is_valid():
            serializer.save()  
            return Response({'status': 'edited'})
        
        print("Erreurs de validation", serializer.errors)


#CREATION BILL
#bill est un num ref, date + client + presta

class CreateClient(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        form = ClientForm(request.data)
        firm = Firm.objects.get(id=1)

        if form.is_valid():
            client = form.save(commit=False)
            client.produced_by = firm
            client.save()

            return Response({'status': 'client created'})
        else:
            return Response({'status': 'errors', 'errors': form.errors})
        
class CreatePresta(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        form = PrestaForm(request.data)

        if form.is_valid():
            prestations = form.save(commit=False)
            prestations.save()

            return Response({'status':'presation created'})
        else:
            return Response({'status': 'errors', 'errors': form.errors})
        


class CreateBill(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request, format=None):
        client_form = ClientForm(request.data)
        PrestaFormSet = formset_factory(PrestaForm)
        presta_formset = PrestaFormSet(request.data, prefix='presta')
        
        if client_form.is_valid() and presta_formset.is_valid():
            firm = Firm.objects.get(created_by=request.user)

            # Création du client
            client = client_form.save(commit=False)
            client.produced_by = firm
            client.save()

            # Création de la facture
            bill = Bill.objects.create(client=client)

            # Création des prestations
            for presta_form in presta_formset:
                prestation = presta_form.save()
                bill.prestation.add(prestation)

            bill.save()
            return Response({'status': 'Bill created'})

        else:
            return Response({'status': 'errors', 'client_errors': client_form.errors, 'presta_errors': [form.errors for form in presta_formset]})




    
        

        



    
