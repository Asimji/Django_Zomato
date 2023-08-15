from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def food_list(request):
    
    food_Items=FoodItems.objects.all()
    return render(request, "food_list.html", context={"food_Items":food_Items})

def add_item(request):

    if request.method=="POST":
        form = foodItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_list')
            
    else: form=foodItemForm()
    return render(request,"add_item.html",context={'form': form})

def update_item(request,pk):
    food_item=get_object_or_404(FoodItems,pk=pk)
    if request.method=="POST":
        form = foodItemForm(request.POST,request.FILES,instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('food_list')

    else: form=foodItemForm(instance=food_item)    

    return render(request,"update.html", {'form':form})    
            
def delete_item(request,pk):
    food_item=get_object_or_404(FoodItems,pk=pk)
    if(request.method=="POST"):
        food_item.delete()
        return redirect('food_list')
    return render(request,"delete.html",{"food_item":food_item})


