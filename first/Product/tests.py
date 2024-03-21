from django.test import TestCase
from.models import Product

# Create your tests here.

class ProductTest(TestCase):

    def setUp(self):
        self.Products=Product.pm.create(Product_name="TestProduct",
                          Product_description="Product has been created for testing",
                          Product_price="500",
                          Product_brand="TestBrand")
        
    def test_create_Product(self):
        Products=Product.pm.get(Product_name="TestProduct")
        self.assertEqual(Products.id,self.Products.id)


    def test_update_Product(self):
        Products=Product.pm.get(Product_name="TestProduct")
        Products.Product_price=5000
        Products.save()

        self.assertNotEqual(Products.Product_price,self.Products.Product_price)


    def test_fetch_product(self):
        Products=Product.pm.all()
        count=len(Products)
        self.assertGreater(count,0)


        
