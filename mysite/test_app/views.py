from django.shortcuts import render
from .forms import RegistrationForm



def reg_view(request):

    reg_form = RegistrationForm() 
    if request.POST:
        if reg_form.is_valid:
            reg_form = RegistrationForm(request)
            reg_form.save()
            reg_form = RegistrationForm()
    args = {
        "reg_form":reg_form,
    }

    return render(request, "index.html", args)

