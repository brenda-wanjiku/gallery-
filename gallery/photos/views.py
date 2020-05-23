from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def homepage(request):
    images = Image.display_images()
    return render(request, 'homepage.html', {'images': images})