from django import forms
from .models import Article, FrontBack

class BatchForms(forms.Form):
    description = forms.CharField(label='Description',
                                  required=False)
    article = forms.ModelChoiceField(queryset=Article.objects.filter(front_back=FrontBack.Frontend.value),
                                     label='Article',
                                     to_field_name='description_article',
                                     required=False)