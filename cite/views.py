from django.shortcuts import render
from .models import Theme, Kurs

def index(request):
    return render(request, 'index.html')

def kurs(request):
    kurs = Kurs.objects.all()
    kategor =  Theme.objects.all()
    return render(request, 'curss.html', {'data': kurs,'model':kategor})

def consul(request):
    return render(request, 'konsul.html')

def otzv(request):
    return render(request, 'otzv.html')

def about(request):
    return render(request, 'about.html')