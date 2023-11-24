from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email_active_code = models.CharField(max_length=100)



class Classification_food(models.Model):
    title =models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Food_menu(models.Model):
    food_name=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    about_food=models.TextField(max_length=1000)
    image = models.ImageField(upload_to='img')
    price=models.IntegerField()
    is_active=models.BooleanField(default=True)
    food_time=models.TimeField(auto_now_add=True)
    Classification=models.ForeignKey('Classification_food',on_delete=models.CASCADE)
    discount=models.IntegerField(null=True,blank=True)
    like = models.ManyToManyField(User)



    def __str__(self):
        return self.food_name
