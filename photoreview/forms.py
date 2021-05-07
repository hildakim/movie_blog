from django import forms
from .models import PhotoReview

class PhotoReviewForm(forms.ModelForm):
    class Meta:
        model = PhotoReview
        fields = ['review_title', 'rating', 'movie', 'image']