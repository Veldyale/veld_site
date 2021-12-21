from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from captcha.fields import CaptchaField

from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('phone',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('phone',)


class AddAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].empty_label = 'Услуга не выбрана'
        self.fields['master'].empty_label = 'Мастер не выбран'
#
    class Meta:
        model = Appointment
        # fields = '__all__'
        fields = ['service', 'master', 'datetime',]


class RegisterUserForm(UserCreationForm):
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-input', 'maxlength': '10',}))
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = CustomUser
        fields = ('phone', 'name', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # captcha = CaptchaField()