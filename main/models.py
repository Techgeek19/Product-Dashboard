from django.db import models

# Create your models here.
class product(models.Model):

    name= models.CharField(max_length=100)
    quantity= models.IntegerField(default=0)
    image= models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name