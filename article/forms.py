from django import forms
from .models import FrontBack, Article, Nomenclature

class ArticleForms(forms.Form):
    numero_article = forms.IntegerField(label='Numéro article')
    description = forms.CharField(label='Description article')
    front_back = forms.ChoiceField(choices=[(tag.value, tag.value) for tag in FrontBack],
                                     label='Front-end / Back-end')
    categorie = forms.CharField(label='Catégorie', required=False)

class AddArticleToNomenclature(forms.Form):
     article = forms.ModelChoiceField(queryset=Article.objects.none())

     def __init__(self, *args, **kwargs):
          id_article = kwargs.pop('id_article', None)
          super(AddArticleToNomenclature, self).__init__(*args, **kwargs)
          if id_article:
            used_ids = Nomenclature.objects.filter(id_article=id_article).values_list('id_nomenclature_id', flat=True)
            available_articles = Article.objects.exclude(id__in=used_ids).filter(front_back=FrontBack.Backend.value)
            self.fields['article'].queryset = available_articles
          else:
               self.fields['article'].queryset = Article.objects.all()