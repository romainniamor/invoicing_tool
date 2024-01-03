from typing import Any
from django.db import models, transaction
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator as minValue
from django.template import defaultfilters
from decimal import Decimal

# Create your models here.

class Firm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    firm_name = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=5)
    website = models.URLField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    siret = models.CharField(max_length=14)
    created_by = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
   
class Client(models.Model):
    produced_by = models.ForeignKey(Firm, on_delete=models.CASCADE, related_name='clients')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Prestation(models.Model):
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(validators=[minValue(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.description
    
    
    @property
    def calculated_total(self):
        total = self.quantity * self.price
        return total
    

class Bill(models.Model):
    num_reference = models.CharField(max_length=10, unique=True)
    created_at = models.DateField(auto_now_add=True)
    prestation = models.ManyToManyField(Prestation, related_name='bills')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='bills')
    payed = models.BooleanField(default=False)


    def __str__(self):
        return self.num_reference
    
    class Meta:
        ordering = ('-created_at', 'payed')

    def created_at_formated(self):
        return defaultfilters.date(self.created_at, 'd M Y')
    

    #modif de la fonction save pr def un num_ref unique + 1 par rapport au precedent dans la liste des bills du client, 
    #lim de 
    def save(self, *args, **kwargs):
        with transaction.atomic():
            #si l utilisateur a au moins une bill alors
            if not self.num_reference:
                #on recup la der
                last_bill = Bill.objects.all().order_by('num_reference').last()
                if last_bill:
                    last_num_reference = last_bill.num_reference
                    #on enleve la premier caractere F et on transforme le reste en int
                    last_number = int(last_num_reference[1:])
                    #auquel ajoute 1
                    new_number = last_number + 1
                else:
                    new_number = 1
                #on ajoute 7 decimales au 7, LIMITE NBRE DE BILL 9 999 999
                self.num_reference = f"F{new_number:07d}"

            super(Bill, self).save(*args, **kwargs)

    