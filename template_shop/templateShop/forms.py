from django import forms
from .models import Imagens

class Foto_form(forms.ModelForm):
    class Meta:
        model = Imagens
        fields = '__all__'