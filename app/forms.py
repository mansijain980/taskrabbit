from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, validators=[EmailValidator(message="Enter a valid email address")],
                             widget = forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already in use")
        return email
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Pass do not match")
        return password2
        
    
    
