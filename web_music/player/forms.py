from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import AddSong


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = AddSong
        fields = ('song',)


# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('description', 'document', )

# class Content(forms.Form):
#     # user = forms.OneToOneField(User, on_delete=models.CASCADE)
#     # song = forms.FileField(upload_to='uploads/songs', blank=True)
#     photo = forms.ImageField(blank=True, upload_to="images/")


# time_created = forms.DateTimeField(auto_now=True)
# song = forms.FileField(upload_to='uploads/songs', blank=True)
# photo = forms.ImageField(null=True, blank=True, upload_to="images/")

#
#
# class LoginUserForm(forms.Form):
#     email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
