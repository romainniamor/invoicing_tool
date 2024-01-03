from django.contrib import admin
from .models import Firm, Client, Prestation, Bill

#https://docs.djangoproject.com/fr/3.2/ref/contrib/admin/#django.contrib.admin.AdminSite


#  user: admin
#  password: admin

#parametre d'en-tete de l'admin
admin.site.site_title = "Facturation Admin"
admin.site.site_header = "Facturation"
admin.site.index_title = "Accueil Administrateur"


#creation data firm
#admin.site.register(Firm)

@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'first_name', 'last_name', 'siret')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('num_reference', 'created_at_formated')

admin.site.register(Prestation)












