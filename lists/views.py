from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
#this uses django render function to build a HttpResponse by taking in the request
#and then searches folders called templates insdie any of the apps directories
#and then builds an HttpResponse based on the content of the template
#Django templates main strength consist of substituting Python variables into
#HTML text which is why the code uses render instead of manually reading the
    return render(request, 'home.html')
