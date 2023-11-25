from django.contrib import admin
from . import models
# Register your models here.


class Food_display(admin.ModelAdmin):
    list_display = ('food_name','is_active','price')
    list_editable = ('is_active','price')


class reserv_display(admin.ModelAdmin):
    list_display = ('name','number_of_guests','date','timee')


class comments_display(admin.ModelAdmin):
    list_display = ('name','email','is_aactive')
    list_editable = ('is_aactive',)

admin.site.register(models.Food_menu,Food_display)
admin.site.register(models.reservation,reserv_display)
admin.site.register(models.Classification_food)
admin.site.register(models.Footer_data)
admin.site.register(models.Comments,comments_display)
