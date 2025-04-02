from django import forms
from datetime import datetime, timedelta
from .models import Article, Lot, StatusOF, FrontBack

class CreateOFForms(forms.Form):
     lot = forms.ModelChoiceField(queryset=Lot.objects.filter(ordrefabrication__isnull=True).order_by('lot'),
                                     label='Lot')
     date_debut = forms.DateField(initial=datetime.today,
                                  label='Date début')
     date_fin = forms.DateField(initial=datetime.today()+timedelta(3),
                                  label='Date fin')
     
class UpdateOFForms(forms.Form):
     date_debut = forms.DateField(label='Date début')
     date_fin = forms.DateField(label='Date fin')
     status_of = forms.ChoiceField(choices=[(tag.value, tag.value) for tag in StatusOF],
                                     label='Status Ordre fabrication')
     
class AddNomenclature(forms.Form):
     article = forms.ModelChoiceField(queryset=Article.objects.none())

     def __init__(self, *args, **kwargs):
          id_ordre_fabrication = kwargs.pop('id_ordre_fabrication', None)
          super(AddNomenclature, self).__init__(*args, **kwargs)
          if id_ordre_fabrication:
               self.fields['article'].queryset = Article.objects.filter(
                    front_back=FrontBack.Backend.value).exclude(
                         articleparlot__id_ordre_fabrication=id_ordre_fabrication).order_by(
                              'numero_article')
          else:
               self.fields['article'].queryset = Article.objects.all()

