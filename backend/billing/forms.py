from django.forms import ModelForm


from .models import Firm, Client, Prestation


class FirmForm(ModelForm):
    class Meta:
        model = Firm
        fields= ('first_name', 'last_name','firm_name','address', 'postal_code', 'city',  'website','phone', 'email','siret',)


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields= ('first_name', 'last_name','address', 'postal_code', 'city')


class PrestaForm(ModelForm):
    class Meta:
        model = Prestation
        fields= ('description', 'quantity','price')

