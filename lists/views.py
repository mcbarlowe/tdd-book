from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.html import escape
from lists.models import Item, List

# Create your views here.
def home_page(request):
#this uses django render function to build a HttpResponse by taking in the request
#and then searches folders called templates insdie any of the apps directories
#and then builds an HttpResponse based on the content of the template
#Django templates main strength consist of substituting Python variables into
#HTML text which is why the code uses render instead of manually reading the
    #item = Item()
    #item.text = request.POST.get('item_text', '')
    #item.save()
#if the site call is a POST method then the site does this
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)

