from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=64)
    # null=True means can be null and blank=True mean is field is not required
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField()
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField()

    def __str__(self):
        return self.title
