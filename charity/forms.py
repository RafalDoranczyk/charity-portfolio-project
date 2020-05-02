from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Donation, Institution
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
        user.first_name = self.cleaned_data["name"]
        user.last_name = self.cleaned_data["surname"]
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


class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = '__all__'

    def save(self, commit=True):
        def save(self, commit=True):
            donation = super(DonationForm, self).save(commit=False)
            donation.quantity = self.cleaned_data['bags']
            inst = int(self.cleaned_data['organization'])
            donation.institution = Institution.objects.get(pk=inst)
            donation.address = self.cleaned_data['address']
            donation.phone_number = self.cleaned_data['phone']
            donation.city = self.cleaned_data['city']
            donation.zip_code = self.cleaned_data['postcode']
            donation.pick_up_date = self.cleaned_data['data']
            donation.pick_up_time = self.cleaned_data['time']
            donation.pick_up_comment = self.cleaned_data['more_info']


