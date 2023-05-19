from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    price= models.IntegerField()

    def __str__(self):
        return self.name