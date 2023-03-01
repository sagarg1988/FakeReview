from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    name=models.CharField(max_length=300)
    typ=models.CharField(max_length=300)
    size=models.IntegerField()
    cost=models.FloatField()
    release_date=models.DateField()
    description=models.TextField(max_length=5000)
    averagerating=models.FloatField(default=0)
    # image = models.URLField(default=None, null=True)
    image = models.ImageField(default='default.jpg', upload_to='product_images/')



    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)],)

    def __str__(self):
        return self.comment
