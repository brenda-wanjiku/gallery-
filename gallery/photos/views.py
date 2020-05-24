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
    return render(request, 'img_location.html', { 'images': images, 'location': img_location} )

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        search_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {'message': message, 'images': search_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})

def single_image(request, id):
    image = Image.get_image_by_id(id = id)
    return render(request,'homepage.html', {'image': image})
    
def location_name(request,id):
    location = get_location(id =id)
    return render('img_location.html', {'location': location})