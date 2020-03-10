from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="head"),
    url(r'kurs/[1-90]?$', views.kurs, name="kurs"),
    path('consul', views.consul, name="consul"),
    path('otzv', views.otzv, name="otzv"),
    path('about', views.about, name="about"),
]