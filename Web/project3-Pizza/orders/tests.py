from django.test import TestCase
from django.contrib.auth.models import User

from .models import Order

# Create your tests here.

class OrdersTest(TestCase):
    #or setUp(self) to creat test db for each test separetely (slower)
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('abcde', 'ab@d', '12345')
        user.first_name = 'Abc'
        user.last_name = 'De'
        user.save()
        
        Order.objects.create(user=User.objects.get(username='abcde'),
                            choice='Regular Pizza',
                            option='1 topping',
                            size='small',
                            price=12.7,
                            extra1='Cheese')
    
    def test_setup(self):
        u = User.objects.all()
        self.assertEqual(u.count(), 1)
        self.assertEqual(u[0].username, 'abcde')

        o = Order.objects.all()
        self.assertEqual(o.count(), 1)
        self.assertEqual(o[0].price, 12.7)

        self.assertEqual(o[0].user, u[0])

    def test_add_extras(self):
        o = Order.objects.get(user='abcde')
        o.extra2 = 'Olives'
        o.save()

        test = Order.objects.get(user='abcde')
        self.assertEqual(test.extra1, 'Cheese')
        self.assertEqual(test.extra2, 'Olives')
        self.assertEqual(test.extra3, '')
    
    def test_dict_to_db(self):
        new_meal = {'user': User.objects.get(username='abcde'),
                    'choice': 'Regular Pizza',
                    'option': '2 toppings',
                    'size': 'small',
                    'price': 15.2}
