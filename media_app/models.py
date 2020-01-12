from django.db import models

class MyModel(models.Model):
    my_image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

