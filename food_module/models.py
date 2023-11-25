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
    Classification=models.ForeignKey('Classification_food',on_delete=models.CASCADE ,blank=False)
    discount=models.IntegerField(null=True,blank=True)
    like = models.ManyToManyField(User,null=True ,blank=True)



    def __str__(self):
        return self.food_name



class Footer_data(models.Model):
    phone_number=models.CharField(max_length=200,blank=True,null=True)
    email=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(max_length=200,blank=True,null=True)
    facebook_link=models.URLField(blank=True,null=True)
    x_link=models.URLField(blank=True,null=True)
    linkdin_link=models.URLField(blank=True,null=True)
    instagram_link=models.URLField(blank=True,null=True)
    pinterest_link=models.URLField(blank=True,null=True)




    def __str__(self):
        return self.phone_number


class reservation(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    number_of_guests= models.IntegerField()
    date=models.DateField(null=True)
    timee=models.TimeField(null=True)

    def __str__(self):
        return self.name




class Comments(models.Model):
    name =models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    text_area =models.TextField(max_length=800)
    is_aactive=models.BooleanField(default=False)


    def __str__(self):
        return self.email