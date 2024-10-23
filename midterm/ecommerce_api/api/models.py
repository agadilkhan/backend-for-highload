from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),  # Create a separate index on 'name'
            models.Index(fields=['price']),  # Create a separate index on 'price'
        ]

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['user']),  # Index on user
            models.Index(fields=['status']),  # Index on order status
            # models.Index(fields=['created_at']),  # Index on order creation time
        ]

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
