from django.contrib import admin
from django.urls import path
from charity.views import (
    LandingView,
    RegisterView,
    LoginView,
    AddDonationView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('donation/', AddDonationView.as_view()),
]
