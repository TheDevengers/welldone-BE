from django import forms
from django.forms import ModelForm
from articles.models import Comment


class CommentForm(ModelForm):
    title = forms.CharField(label="Title")
    text = forms.CharField(label="Text", widget=forms.Textarea(attrs={'rows': 10}))

    class Meta:
        model = Comment
        fields = ['title', 'text']

