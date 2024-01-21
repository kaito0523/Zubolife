from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/',blank=True, null=True, name="image")
    content = models.TextField(max_length=140, null=True,blank=True)
    zairyou = models.TextField(max_length=392,null=True,blank=True)
    tukurikata = models.TextField(max_length=1000, null=True,blank=True)
    sankou = models.URLField(max_length=100, null=True,blank=True)

class Memo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(null=True)
    
