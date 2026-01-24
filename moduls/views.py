from django.shortcuts import render

from djago.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse("Hello, World!")

python manage.py shell
from accounts.models import books, foods