from django.forms import ModelForm
from django import forms

from articleapp.models import TbName
# from newsapp.models import News


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))
    ariticle = forms.ModelChoiceField(queryset=TbName.objects.all(), required=False)

    class Meta:
        model = TbName
        fields = ['code', 'name', 'market', 'sector','listed_date','CEO','market_cap']