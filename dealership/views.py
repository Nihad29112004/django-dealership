from django.shortcuts import render
from .models import Dealer  # bayi modelinin adı Dealer ise

def home(request):
    dealers = Dealer.objects.all()  # tüm bayileri çek
    return render(request, 'dealership/home.html', {'dealers': dealers})
