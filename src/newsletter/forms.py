from django import forms
from .models import Signup

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not domain == 'genscript':
            raise forms.ValidationError("We accept only Genscript Email Account")
        return email