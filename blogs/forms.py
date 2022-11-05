from django import forms
from django import forms

from .models import BlogPost, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        labels = {'title': 'Your title', 'content': ''}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}