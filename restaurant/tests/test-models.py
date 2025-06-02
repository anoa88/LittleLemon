from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice", price=80, inventory=100)
        self.assertEqual(item, "Ice : 80")