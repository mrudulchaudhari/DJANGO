from django.contrib import admin

# Register your models here.
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate

admin.site.register(ChaiVariety)