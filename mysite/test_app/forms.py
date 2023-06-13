from .models import Person
from django.forms import forms
from .models import Olymp



class RegistrationForm(forms.Form):
    name = forms.CharField(verbose_name="Имя", max_length=150, required = True)
    surname = forms.CharField(verbose_name="Фамилия", max_length=150, required = True)
    patronymic = forms.CharField(verbose_name="Отчество", max_length=150, required = False)
    test = forms.ChoiceField(Olymp, verbose_name="Олимпиада", max_length=150)
   


