from django import forms
from .models import Review

class MovieForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('product', 'user', 'comment', 'rating')



