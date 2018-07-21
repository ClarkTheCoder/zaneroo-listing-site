from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'price',
            'title',
            'body',
            'contact_email',
            'contact_number',
            'picture',
        )
        widgets = {
            'price': forms.TextInput(attrs={'placeholder': 'Price'}),
            'title': forms.TextInput(attrs={'placeholder': 'Item for sale'}),
            'body': forms.Textarea(attrs={'placeholder': 'Describe the item'}),
            'contact_email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
        }
