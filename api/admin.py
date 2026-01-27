from django.contrib import admin
from .models import Contact, Donation, LoginActivity

admin.site.register(Contact)
admin.site.register(Donation)
admin.site.register(LoginActivity)
