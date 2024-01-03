from rest_framework import serializers
from .models import Firm, Client, Prestation, Bill, User

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        created_by = User
        fields= ('id','first_name', 'last_name','firm_name','address', 'postal_code', 'city',  'website','phone', 'email','siret', 'created_by',)

class ClientSerializer(serializers.ModelSerializer):
    produced_by = FirmSerializer()
    class Meta:
        model = Client
        fields= ('id','first_name', 'last_name','address', 'postal_code', 'city', 'produced_by')


class PrestationSerializer(serializers.ModelSerializer):
    calculated_total = serializers.SerializerMethodField()
    class Meta:
        model = Prestation
        fields= ('id','description', 'quantity','price','calculated_total')

    def get_calculated_total(self, obj):
        return obj.calculated_total
    
class BillSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    prestation = PrestationSerializer(many=True)
 
    class Meta:
        model = Bill
        fields= ('id','num_reference', 'created_at_formated', 'client', 'prestation', 'payed')




