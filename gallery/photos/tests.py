from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.


class CategoryTestClass(TestCase):

    def setUp(self) -> None:
        # creating a new location and saving it
        self.new_category = Category(category='nature')
        self.new_category.save_category()

    def tearDown(self):
        '''
        Clears database after each test
        '''
        Category.objects.all().delete()

    def test_save_location(self):
        '''
        Tests whether the category is saved
        '''
        self.new_category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_category(self):
        '''
        Tests whether the category is deleted
        '''
        self.new_category.delete_category()
        category = Category.objects.all()
        self.assertEqual(len(category), 1)

    def test_update_category(self):
        '''
        Tests whether the category is updated
        '''
        self.new_category.save_category()
        updated_category = Category.update_category(
            self.new_category.id, 'Food')
        self.assertEqual(updated_category.category, 'Food')


class LocationTestClass(TestCase):

    def setUp(self):
        # creating a new location and saving it
        self.new_location = Location(location='Nairobi')
        self.new_location.save()

    def tearDown(self):
        '''
        Clears database after each test
        '''
        Location.objects.all().delete()

    def test_save_location(self):
        '''
        Tests whether the location is saved
        '''
        self.new_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_location(self):
        '''
        Tests whether the location is deleted
        '''
        self.new_location.save_location()
        self.new_location.delete_location()
        location = Location.objects.all()
        self.assertEqual(len(location), 0)

    def test_update_location(self):
        '''
        Tests whether the location is updated
        '''
        self.new_location.save_location()
        updated_location = Location.update_location(self.new_location.id, 'Mombasa')
        self.assertEqual(updated_location.location, 'Mombasa')


class ImageTestClass(TestCase):

    def setUp(self):
        # creating a new location and saving it
        self.new_location = Location(location='Nairobi')
        self.new_location.save()

        # creating a new category and saving it
        self.new_category = Category(category='nature')
        self.new_category.save()

        # creating a new image and saving it
        self.new_image = Image(name="birthday21", description="Turns 21", image_pic="photo.jpeg",
                               img_category=self.new_category, img_location=self.new_location)
        self.new_image.save_image()

    def tearDown(self):
        '''
        Clears database after each test
        '''
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):
        '''
        This will test whether the new objects created is an instance of the classes 
        '''
        self.assertTrue(isinstance(self.new_image, Image))
        self.assertTrue(isinstance(self.new_location, Location))
        self.assertTrue(isinstance(self.new_category, Category))

    def test_save_image(self):
        '''
        Tests whether the location is saved
        '''
        self.new_image.save_image()
        self.new_location.save()
        self.new_category.save()
        locations = Location.objects.all()
        categories = Category.objects.all()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
        self.assertTrue(len(categories) > 0)
        self.assertTrue(len(locations) > 0)

    def test_filter_by_location(self):
        '''
        Tests whether Image can be accessed using location
        '''
        self.new_image.save_image()
        img_location = Image.filter_by_location(self.new_image.img_location == img_location)
        self.assertEqual(img_location.location, "Nairobi")

    def test_get_image_by_id(self):
        '''
        Tests whether image is retrieved by id 
        '''
        self.new_image.save_image()
        image = Image.get_image_by_id(self.new_image.id)
        self.assertEqual(image.name, self.new_image.name)
)

    def test_search_image_by_category(self):
        '''
        Tests whether the image can be searched by category
        '''
        self.new_image.save_image()
        image_category = Image.search_image(self.new_image.img_category.category)
        self.assertEqual(image_category.img_category.category, 'nature')

    def test_update_image(self):
        '''
        Tests whether the image can be updated
        '''
        self.new_image.save_image()
        updated_image = Image.update_image(self.new_image.id, 1)
        self.assertEqual(updated_image.image_pic, 'photo.jpeg')
