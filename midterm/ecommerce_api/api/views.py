from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.core.cache import cache
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])
def product_list(request):
    cached_products = cache.get('product_list')

    if cached_products is None:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        cached_products = serializer.data

        cache.set('product_list', cached_products, timeout=60 * 15)

    return Response(cached_products)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create orders

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Save order for the logged-in user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
