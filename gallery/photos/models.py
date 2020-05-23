from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length = 30)

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

    def __str__(self):
        return self.location

    def save_location(self):
        return self.save()

    def delete_location(self):
        return self.delete()

    @classmethod
    def update_location(cls, id, location):
        cls.objects.filter(id = id).update( location = location)
        updated_location = cls.objects.get(id = id)
        return updated_location


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
        cls.objects.filter( id = id).update( image_pic = image_pic)
        update_image = cls.objects.get(id = id)
        return update_image

    @classmethod
    def display_images(cls):
        images = cls.objects.all()
        return images





