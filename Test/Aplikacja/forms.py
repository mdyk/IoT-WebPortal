from django import forms
from .models import Urzadzenie

class UrzadzenieForm(forms.ModelForm):

    class Meta:
        model = Urzadzenie
        fields=('Nazwa', 'RodzajPlatformy', 'AdresIP', 'Prywatnosc', 'Stan')
