from decimal import Decimal
from django.test import TestCase
from product.models import Category
from product.serializers.product_serializer import ProductSerializer

class TestProductSerializer(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Hardware", active=True)
        self.product_data = {
            "title": "Mouse Gamer",
            "description": "RGB 16000 DPI",
            "price": Decimal('250.00'),
            "active": True,
            "categories_id": [self.category.id]
        }

    def test_create_product_with_categories(self):
        serializer = ProductSerializer(data=self.product_data)
        if not serializer.is_valid():
            print(serializer.errors)  
        self.assertTrue(serializer.is_valid())
        product = serializer.save()

        self.assertEqual(product.title, "Mouse Gamer")
        self.assertEqual(product.category.count(), 1)
        self.assertEqual(product.category.first().id, self.category.id)