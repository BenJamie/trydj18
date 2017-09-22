from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "timestamp"]
    form = SignUpForm
    # class Meta:
    #     model = Signup

admin.site.register(Signup, SignupAdmin)