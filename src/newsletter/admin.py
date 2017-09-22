from django.contrib import admin

# Register your models here.
from .models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "full_name", "email"]
    class Meta:
        model = Signup

admin.site.register(Signup, SignupAdmin)