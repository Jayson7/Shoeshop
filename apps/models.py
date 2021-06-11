from django.db import models

# Create your models here.

# product

class Product(models.Model):
      name = models.CharField(max_length=300)
      price = models.PositiveIntegerField()
      poster = models.FileField(upload_to="images")

      def __str__(self):
            return self.name
      
class Cartitem(models.Model):
      name = models.ForeignKey(Product, on_delete=models.CASCADE)
     

      def __str__(self):
            
            return self.name 
      