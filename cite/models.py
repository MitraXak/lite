from django.db import models
from django.utils import timezone
#Пользователи
class Users(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.login
#Курсы
class Kurs(models.Model):
    name = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.name
class Theme(models.Model):
    nametheme = models.ForeignKey(Kurs, on_delete = models.CASCADE)
    namekat = models.CharField(max_length=100)
    publishedkat_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.publishedkat_date = timezone.now()
        self.save()
    def __str__(self):
        return self.namekat
#Связь пользователей и курсы
class UserKur(models.Model):
    logi_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    namekurs = models.ForeignKey(Kurs, on_delete = models.CASCADE)
    def __str__(self):
        return self.user.login



