from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

SIGNUP_FORM_CLASS = 'w-100 mb-2 pb-2'
class loginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.PasswordInput()
class signupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': f'{SIGNUP_FORM_CLASS} w-100 pb-2', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class': f'{SIGNUP_FORM_CLASS} w-100 pb-2', 'placeholder': 'Re-enter your password'})
        
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={

                'class':SIGNUP_FORM_CLASS,
                'placeholder':'Enter your username'
            }),
            'email':forms.TextInput(attrs={

                'class':SIGNUP_FORM_CLASS,
                'placeholder':'Enter your email'
            }),
            }

