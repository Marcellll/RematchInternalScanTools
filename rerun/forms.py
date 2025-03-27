from django import forms

class RerunForms(forms.Form):
    numero_pesee = forms.IntegerField(label='Numero de pesee', min_value=330110000)