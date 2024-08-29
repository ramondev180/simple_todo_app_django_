from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django  import forms
from .models import User


class UserRegistrationForm(forms.Form):
    
    # password1 = None
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','email', 'last_name']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Confirm password must be the same")
        elif len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        return confirm_password
    
    def save(self):
        user = User()
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user