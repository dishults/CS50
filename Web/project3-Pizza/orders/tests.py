from django.test import TestCase
from django.contrib.auth.models import User

from .models import Pending, Placed

# Create your tests here.

class OrdersTest(TestCase):
    #or setUp(self) to creat test db for each test separetely (slower)
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('abcde', 'ab@d', '12345')
        user.first_name = 'Abc'
        user.last_name = 'De'
        user.save()
        user = User.objects.create_user('12345', '12@d', '12345')
        user.first_name = '123'
        user.last_name = '12'
        user.save()
        
        Pending.objects.create(user=User.objects.get(username='abcde'),
                            choice='Regular Pizza',
                            option='1 topping',
                            size='small',
                            price=12.7,
                            extra1='Cheese')
        Pending.objects.create(user=User.objects.get(username='abcde'),
                            choice='Sicilian Pizza',
                            option='1 topping',
                            size='small',
                            price=12.7,
                            extra1='Cheese')
    
    def test_setup(self):
        u = User.objects.all()
        self.assertEqual(u.count(), 2)
        self.assertEqual(u[0].username, 'abcde')
        self.assertEqual(u[1].username, '12345')

        o = Pending.objects.all()
        self.assertEqual(o.count(), 2)
        self.assertEqual(o[0].price, 12.7)

        self.assertEqual(o[0].user, u[0])
        self.assertEqual(o[1].user, u[0])

    def test_add_extras(self):
        o = Pending.objects.filter(user='abcde')
        o1 = o[0]
        o1.extra2 = 'Olives'
        o1.save()

        test = Pending.objects.filter(user='abcde')
        self.assertEqual(test[0].extra1, 'Cheese')
        self.assertEqual(test[0].extra2, 'Olives')
        self.assertEqual(test[0].extra3, '')
        self.assertEqual(test[1].choice, 'Sicilian Pizza')
    
    def test_delete_db_entry(self):
        o = Pending.objects.filter(user='abcde')
        self.assertEqual(o.count(), 2)

        o1 = o[1]
        o1.delete() # o.delete() to delete everything

        o = Pending.objects.filter(user='abcde')
        self.assertEqual(o.count(), 1)

        Pending.objects.get(pk=1).delete()
        
        o = Pending.objects.filter(user='abcde')
        self.assertEqual(o.count(), 0)
    
    def test_archive_order(self):
        o = Pending.objects.all()
        p = Placed.objects.all()
        self.assertEqual(o.count(), 2)
        self.assertEqual(p.count(), 0)

        o = Pending.objects.get(pk=1)
        Placed.objects.create(user=o.user,
                                choice=o.choice,
                                option=o.option,
                                size=o.size,
                                price=o.price,
                                extra1=o.extra1)

        p = Placed.objects.all()
        self.assertEqual(p.count(), 1)
        
        o.delete()
        o = Pending.objects.all()
        p = Placed.objects.all()
        self.assertEqual(o.count(), 1)
        self.assertEqual(p.count(), 1)

