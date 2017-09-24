from django.shortcuts import render
from .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New Full Name"
        instance.full_name = full_name
        # if not instance.full_name:
        #     instance.full_name = "Ben"
        instance.save()
        context = {
            "title": "Thank You!"
        }
    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        for key, value in form.cleaned_data.items():
            print(key, value)
        # full_name = form.cleaned_data.get("full_name")
        # email = form.cleaned_data.get("email")
        # message = form.cleaned_data.get("message")

        # print(full_name, email, message)

    return render(request, "contact.html", context)
