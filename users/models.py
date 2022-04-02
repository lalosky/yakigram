from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    website      =  models.URLField(max_length=254)
    biography    =  models.TextField()
    phone_number =  models.CharField(max_length=50, blank=True, null=True)

    picture = models.ImageField(upload_to='users/pictures/', blank=True, null=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user.username