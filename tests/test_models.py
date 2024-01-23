from django.test import TestCase
from restaurant.models import Menu

#TestCase class
class MenuTest(TestCase):
    def test_get_items(self):
        item = Menu.objects.create(title="IceCream", price=100, inventory=50)
        self.assertEqual(item.__str__(), "IceCream: 100")