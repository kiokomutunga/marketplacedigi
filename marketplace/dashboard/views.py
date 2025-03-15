from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item,Category

@login_required
def index(request):
    items = Item.objects.filter(created_by = request.user)
    return render(request,'indexx.html',{
        'items':items,
    }) 
@login_required
def index(request):
    
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request,'index.html',{
        'categories': categories, 'items': items,
    })

