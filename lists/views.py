from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

'''
def home_page(request):
    item = Item()
    # 从 request.POST 字典中获取键 item_text 对应的值，并将其赋值给 item.text
    item.text = request.POST.get('item_text', '')
    item.save()

    return render(request, 'home.html', {
        'new_item_text': item.text if request.method == 'POST' else ''
    })
    # return HttpResponse('<html><title>To-Do lists</title></html>')
'''
def home_page(request):
    '''if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-new-page/')'''
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-new-page/')
