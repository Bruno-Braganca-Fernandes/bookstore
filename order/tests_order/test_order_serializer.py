from django.test import TestCase
from django.contrib.auth.models import User
from product.models import Product
from order.serializers.order_serializer import OrderSerializer

class TestOrderSerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alex", password="123")
        self.product_1 = Product.objects.create(title="Teclado", price=150, active=True)
        self.product_2 = Product.objects.create(title="Monitor", price=900, active=True)
        
        self.order_data = {
            "user": self.user.id,
            "products_id": [self.product_1.id, self.product_2.id]
        }

    def test_order_total_calculation(self):
        serializer = OrderSerializer(data=self.order_data)
        self.assertTrue(serializer.is_valid())
        order = serializer.save()
        
        self.assertEqual(serializer.data["total"], 1050)

    def test_order_creation_logic(self):
        serializer = OrderSerializer(data=self.order_data)
        self.assertTrue(serializer.is_valid())
        order = serializer.save()
        
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.product.count(), 2)