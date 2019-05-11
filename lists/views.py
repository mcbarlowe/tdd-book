from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

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
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
