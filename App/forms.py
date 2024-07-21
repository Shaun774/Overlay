from django import forms
from .models import Photo

class Photoform(forms.ModelForm):
    class Meta:
        model = Photo
        fields =["image"]