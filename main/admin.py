from django.contrib import admin
from .models import CarMake, CarModel,Dealer
admin.site.register(Dealer)
admin.site.register(CarMake)
admin.site.register(CarModel)
