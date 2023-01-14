from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from newsapp.models import News


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=News.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'content']