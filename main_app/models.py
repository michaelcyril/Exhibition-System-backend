from django.db import models
from authUser.models import User


# Create your models here.


class Exhibition(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "exhibition"


class Block(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        db_table = "block"


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f''
