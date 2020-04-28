from django.shortcuts import render
from django.views import View


class LandingView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


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