from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.SmallIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.name}: {self.booking_date.strftime}'
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.title}: {self.price}'

