from django.contrib import admin
from .models import VerificationCode, Profile, Contact

admin.site.register(VerificationCode)
admin.site.register(Contact)
admin.site.register(Profile)

# Register your models here.
