from django.db import models

# Create your models here.

class FoodItems(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    image=models.ImageField(upload_to='FoodItems')
    def __str__(self) -> str:
        return self