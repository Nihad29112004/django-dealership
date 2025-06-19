from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=20)  # Məsələn: 'active', 'inactive'

    def __str__(self):
        return self.name

class Review(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review by {self.author} for {self.dealer.name}'
