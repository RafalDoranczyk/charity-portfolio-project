from django.contrib import admin
from .models import Category, Institution, Donation

admin.site.register({Category, Institution, Donation})