from django import forms
from pagedown.widgets import PagedownWidget
from . models import post
class PostForm(forms.ModelForm):
    context=forms.CharField(widget=PagedownWidget)
    class Meta:
        model=post
        fields=["title","context","image"]

