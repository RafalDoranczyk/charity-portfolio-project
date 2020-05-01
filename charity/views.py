from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from .models import Donation, Institution
from django.contrib.auth import login
from django.db.models import Sum
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User


class LandingView(View):
    template_name = 'index.html'

    def get(self, request):
        bags_number = Donation.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
        organiation_number = Donation.objects.values('institution_id').distinct('institution').count()
        insitution_types = Institution.INSTITUTION_TYPE_CHOICES
        ctx = {
            'bags_number': bags_number,
            'organiation_number': organiation_number,
            'insitution_types': insitution_types
        }
        return render(request, self.template_name, ctx)


class AddDonationView(View):
    template_name = 'form.html'

    def get(self, request):
        return render(request, self.template_name)


def auth_login(password, email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user

    return None


class LoginView(LoginView):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth_login(password, email)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            ctx = {
                'msg': 'brak użytkownika'
            }
            return render(request, self.template_name, ctx)
        return render(request, self.template_name)


class RegisterView(View):
    fields = '__all__'
    template_name = "register.html"
    form_class = UserForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password2']
            user.set_password(password)
            user.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})


class LogoutView(LogoutView):
    template_name = 'index.html'