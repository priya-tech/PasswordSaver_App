from django.db import models

# Create your models here.
class AddPasswordModel(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    id=models.AutoField(primary_key=True)
