from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    img_link = models.URLField(max_length=999)
    category = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    product_slug = AutoSlugField(populate_from='title', unique=True, null=True)

    def __str__(self):
        return self.title    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.quantity * self.product.price
    
class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
