from django.contrib import admin
from django.urls import path

from charity.api import CategoriesAPI, DonationAPI, InstitutionsAPI
from charity.views import (
    LandingView,
    RegisterView,
    LoginView,
    AddDonationView,
    LogoutView,
    FormConfirmationView,
    UserView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingView.as_view(), name='landing'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('donation/', AddDonationView.as_view(), name='donation_form'),
    path('confirm/', FormConfirmationView.as_view(), name='form_confirmation'),
    path('user/', UserView.as_view(), name='user'),
    path('api/categories/', CategoriesAPI),
    path('api/donation/', DonationAPI),
    path('api/institutions/', InstitutionsAPI)
]
