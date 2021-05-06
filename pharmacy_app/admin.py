
# Register your models here.
from django.apps import AppConfig
from django.contrib import admin
from .models import Pharmacist , Customer , Doctor , Medicine, Billing, Entry

admin.site.register(Pharmacist)
admin.site.register(Customer)
admin.site.register(Doctor)
admin.site.register(Medicine)
admin.site.register(Billing)
admin.site.register(Entry)