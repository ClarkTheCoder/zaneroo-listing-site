from django import forms
from accounts import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistraionForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
            )

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirm'}),
            }

    def save(self, commit=True):
        user = super(RegistraionForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
                'email',
                'first_name',
                'last_name',
                'password'
             )

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            }



class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'

        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Motto'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'website': forms.TextInput(attrs={'placeholder': 'Website/Brand'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            }
