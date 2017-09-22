from django.contrib import admin

# Register your models here.
from .models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "timestamp"]
    class Meta:
        model = Signup

admin.site.register(Signup, SignupAdmin)