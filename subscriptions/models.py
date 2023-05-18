from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price= models.IntegerField()

    def __str__(self):
        return self.name