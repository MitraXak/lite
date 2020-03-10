from django.contrib import admin
from .models import Users, Kurs, UserKur, Theme
# Register your models here.
admin.site.register(Users)
admin.site.register(Kurs)
admin.site.register(UserKur)
admin.site.register(Theme)