from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu  
from restaurant.serializers import MenuSerializer  


class MenuViewTest(TestCase):
    
    def setUp(self):
        """
        La méthode setUp() est appelée avant chaque test.
        Nous y ajoutons quelques objets Menu à la base de données pour les tests.
        """
        # Création de quelques objets Menu pour les tests
        Menu.objects.create(title="Pizza", price=10, inventory=50)
        Menu.objects.create(title="Burger", price=5, inventory=100)

    def test_get_all_menus(self):
        """
        Teste la vue qui récupère tous les objets Menu.
        """
        # L'URL de l'API pour récupérer tous les menus
        url = reverse('menu-list')  # Assure-toi que l'URL est correctement définie dans `urls.py`

        # Effectuer la requête GET
        client = APIClient()
        response = client.get(url)

        # Vérification du statut de la réponse
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Sérialisation des objets Menu créés dans `setUp()`
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Vérification que les données sérialisées correspondent à la réponse
        self.assertEqual(response.data, serializer.data)
