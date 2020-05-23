from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def homepage(request):
    images = Image.display_images()
    return render(request, 'homepage.html', {'images': images})

def get_location(request, img_location):
    '''
    Function that filters images by location
    '''
    images = Image.filter_by_location(img_location = img_location)
    return render(request, 'img_location.html', { 'images': images } )