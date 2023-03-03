from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
     def setUp(self):
         self.client = APIClient()
         self.menu1 = Menu.objects.create(id = 11, title="Pizza", price=10.99, inventory=100)
         self.menu2 = Menu.objects.create(id = 12, title="Burger", price=8.99, inventory=100)

     def test_getall(self):
         response = self.client.get(reverse('menu-list'))
         menus = Menu.objects.all()
         serializer = MenuSerializer(menus, many=True)
         self.assertEqual(response.data, serializer.data)
         self.assertEqual(response.status_code, status.HTTP_200_OK)