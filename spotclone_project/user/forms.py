from django.contrib.auth import forms as auth_forms, get_user_model
from django.core import validators
from django import forms
from .models import Profile

User = get_user_model()
class RegisterForm(auth_forms.UserCreationForm):
    
    username = forms.CharField(
        label='Username',
        validators=[validators.MinLengthValidator(3),
                    validators.MaxLengthValidator(30)]
        )
    
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'blank':False,
                                       'null':False,
                                       })
    )
    
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        validators=[validators.RegexValidator(
            regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$',
            message="Password must be at least 8 characters long and contain both letters and numbers."
        )]
    )
    password2 = forms.CharField(
        label='Confirm Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    widgets = {
        'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
    }
    
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','username', 'email','date_of_birth']  # Add any other fields you want to display in the form

    # Set the widget for the date_of_birth field
    widgets = {
        'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
    }
class DeleteUserForm(forms.Form):
    confirm_delete = forms.BooleanField(
        label='Confirm Deletion',
        required=True,
    )
    
class AddImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
