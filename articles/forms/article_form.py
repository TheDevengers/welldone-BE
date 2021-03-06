from django import forms
from django.forms import ModelForm
from articles.models import Article, Category

DRAFT = 'DR'
PUBLISHED = 'PB'

ART_STATE = {
    (DRAFT, 'No'),
    (PUBLISHED, 'Yes'),
}

class ArticleForm(ModelForm):
    title = forms.CharField(label="Title")
    introduction = forms.CharField(label="Intro")
    body = forms.CharField(label="Body", widget=forms.Textarea(attrs={'rows': 10}))
    categories = forms.ModelMultipleChoiceField(label="Category (Ctrl + click to multiple selection)", queryset=Category.objects.all(), widget=forms.SelectMultiple)
    image = forms.URLField(required=False)
    state = forms.ChoiceField(
        label="Publish ?",
        choices=ART_STATE
    )

    class Meta:
        model = Article
        fields = ['id', 'title', 'introduction', 'body', 'categories', 'image', 'state']


