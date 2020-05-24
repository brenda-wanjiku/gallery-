from django.db import models

# Create your models here.
class Category(models.Model):
    CATEGORY_CHOICES=[
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Architecture', 'Architecture'),
        ('Fashion', 'Fashion'),
        ('Arts', 'Arts'),
    ]
    category = models.CharField(max_length = 30, choices=CATEGORY_CHOICES, default='Travel')

    def __str__(self):
        return self.category

    def save_category(self):
        return self.save()

    def delete_category(self):
        return self.delete

    @classmethod
    def update_category(cls, id, category):
        cls.objects.filter(id = id).update( category = category)
        updated_category = cls.objects.get(id = id)
        return updated_category



class Location(models.Model):
    location = models.CharField(max_length = 30)

    
    def save_location(self):
        return self.save()

    def delete_location(self):
        return self.delete()

    @classmethod
    def update_location(cls, id, location):
        cls.objects.filter(id = id).update( location = location)
        updated_location = cls.objects.get(id = id)
        return updated_location

    @classmethod
    def get_location(cls,id):
        location = Location.objects(id=id)
        return location
    
    def __str__(self):
        return self.location


class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length = 30)
    image_pic = models.ImageField(upload_to='photos/', null=True)
    img_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, image_pic, id):
        cls.objects.filter( id = id).update(image_pic = image_pic)
        update_image = cls.objects.get(id = id)
        return update_image

    @classmethod
    def display_images(cls):
        images = cls.objects.all()
        return images


    @classmethod
    def filter_by_location(cls,img_location):
       photo_location = cls.objects.filter(img_location=img_location)
       return photo_location

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(img_category__category__icontains=search_term)
        return images

