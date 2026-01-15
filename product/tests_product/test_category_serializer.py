from django.test import TestCase
from product.serializers.category_serializer import CategorySerializer

class TestCategorySerializer(TestCase):
    def setUp(self):
        self.category_data = {
            "name": "Tecnologia",
            "slug": "tecnologia",
            "description": "Produtos tech",
            "active": True
        }

    def test_valid_category_serializer(self):
        serializer = CategorySerializer(data=self.category_data)
        self.assertTrue(serializer.is_valid())

    def test_category_slug_is_optional(self):
        data_no_slug = self.category_data.copy()
        data_no_slug.pop("slug")
        serializer = CategorySerializer(data=data_no_slug)
        self.assertTrue(serializer.is_valid())