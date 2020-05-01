from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserForm(UserCreationForm):
    name = forms.CharField(max_length=128)
    surname = forms.CharField(max_length=128)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["name", "surname", "email", "password1", "password2"]
        USERNAME_FIELD = 'email'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.name = self.cleaned_data["name"]
        user.surname = self.cleaned_data["surname"]
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["email"]

        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        try:
            User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return cleaned_data
        raise forms.ValidationError('email znajduje się w bazie')