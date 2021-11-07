from django.db import models

from users.models import User

class ProductCategory (models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class ProductSubcategory (models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Product Subcategories'

    def __str__(self):
        return f'{self.name} | {self.category.name} '



class Product (models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField (upload_to = 'products_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(ProductSubcategory, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} | {self.category.name} | {self.subcategory.name}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price