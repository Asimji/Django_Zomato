from django import forms

from .models import *

class foodItemForm(forms.ModelForm):
     class Meta:
          model=FoodItems
          fields=['name', 'description', 'price', 'image']
          
