from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from django.db.models import Q
from .forms import NewItemForm,EditItemForm

def items(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_id:
        items = items.filter(category_id=category_id)


    return render(request,'items.html',{
        'items':items,
        'query':query,
         'categories':categories,
         'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'detail.html',{
        'item':item,
        'related_items':related_items
    })
@login_required
def new(request):
    if request.method =='POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail',pk=item.id)
    else:
        form = NewItemForm()

    return render(request,'itemform.html',{
        'form':form,
        'title':'New item'
    })
@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk,created_by = request.user)
    if request.method =='POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()

            return redirect('item:detail',pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request,'itemform.html',{
        'form':form,
        'title':'Edit item',
    })

@login_required
def delete(request, pk):

    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    
    if request.method == "POST":
        item.delete()
        return redirect('dashboard:index')

    return render(request, 'confirm_delete.html', {'item': item})
