from django import forms
from .models import Article, FrontBack, Lot

class BatchForms(forms.Form):
    description = forms.CharField(label='Description')
    article = forms.ModelChoiceField(queryset=Article.objects.filter(front_back=FrontBack.Frontend.value),
                                     label='Article',
                                     to_field_name='description_article',
                                     required=False)
    
class NewBatchForms(forms.Form):
    lot = forms.IntegerField(label='Numéro de lot', initial=Lot.objects.filter(lot__startswith=330).order_by('-lot').first().lot+1)
    description = forms.CharField(label='Description')
    article = forms.ModelChoiceField(queryset=Article.objects.filter(front_back=FrontBack.Frontend.value),
                                     label='Article',
                                     to_field_name='description_article',
                                     required=False)