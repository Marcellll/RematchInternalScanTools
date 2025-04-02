from django import forms

from .models import ChargementStatus

class UpdateChargementForms(forms.Form):
    status_chargement = forms.ChoiceField(choices=[(tag.value, tag.value) for tag in ChargementStatus],
                                     label='Status Chargement')
    date_debut = forms.DateField(label='Date de début')
    date_fin = forms.DateField(label='Date de fin')

class NewCamionForms(forms.Form):
    description = forms.CharField(label='Description')