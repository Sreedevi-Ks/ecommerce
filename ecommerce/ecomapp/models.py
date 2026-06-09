from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):

        return self.email

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=500)
    def __str__(self):

        return self.name
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_amount = models.IntegerField()

    def __str__(self):

        return self.user.email
class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    total = models.IntegerField()

    status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)

    def __str__(self):

        return self.user.email