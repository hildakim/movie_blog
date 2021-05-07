from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['review_title', 'nickname', 'review_body', 'movie', 'image']