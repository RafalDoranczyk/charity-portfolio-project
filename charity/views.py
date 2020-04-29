from django.shortcuts import render
from django.views import View
from .models import Donation
from django.db.models import Sum


class LandingView(View):
    template_name = 'index.html'

    def get(self, request):
        bags_number = Donation.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
        organiation_number = Donation.objects.values('institution_id').distinct('institution').count()
        ctx = {
            'bags_number': bags_number,
            'organiation_number': organiation_number
        }
        return render(request, self.template_name, ctx)


class AddDonationView(View):
    template_name = 'form.html'

    def get(self, request):
        return render(request, self.template_name)


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)