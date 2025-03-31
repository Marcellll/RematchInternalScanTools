from django import forms
from .models import FrontBack

class ArticleForms(forms.Form):
    numero_article = forms.IntegerField(label='Numéro article')
    description = forms.CharField(label='Description article')
    front_back = forms.ChoiceField(choices=[(tag.name, tag.value) for tag in FrontBack],
                                     label='Front-end / Back-end')
    categorie = forms.CharField(label='Catégorie', required=False)