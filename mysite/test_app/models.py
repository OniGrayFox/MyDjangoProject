from django.db import models
from django.utils import timezone


# Create your models here.
class Olymp(models.Model):
    name = models.CharField(verbose_name="Наименование олимпиады", max_length=150)
    subject = models.CharField(verbose_name="Предмет", max_length=150)
    start_time = models.DateTimeField(verbose_name="Время проведения", default=timezone.now, blank=True)
    end_time = models.DateTimeField(verbose_name="Время проведения", blank=True)


    class Meta:
        verbose_name = "Олимпиады"


    def __str__(self):
        return self.name




class Person(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=150)
    surname = models.CharField(verbose_name="Фамилия", max_length=150)
    patronymic = models.CharField(verbose_name="Отчество", max_length=150, blank=True)
    is_checker = models.BooleanField(verbose_name="является проверяющим?", default=False)
    test = models.ManyToManyField(Olymp, verbose_name="Олимпиада", max_length=150)
    answer = models.FileField(upload_to="/media/answers" , verbose_name="Файл ответа")

    class Meta:
        verbose_name = "Олимпиады"


    def __str__(self):
        return f"{self.surname}{self.name}{self.patronymic}"



class Result(models.Model):
    person = models.ForeignKey(Person, verbose_name="ФИО")
    olymp = models.ForeignKey(Olymp, verbose_name="Олимпиада")
    result = models.CharField(verbose_name="Фамилия", max_length=150)


    class Meta:
        verbose_name = "Результаты"


    def __str__(self):
        return f"{self.person}"