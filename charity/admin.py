from django.contrib import admin
from .models import Category, User, Institution, Donation
# Register your models here.

admin.site.register({Category, Institution, Donation})