from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
from django.http import JsonResponse
def get_products_from_db(request):
    data = list(Product.objects.values('Title', 'Description', 'Price'))
    return JsonResponse(data, safe=False)