from django.contrib import admin
from .import models
# Register your models here.
@admin.register(models.Restaurants)
class Customer_admin(admin.ModelAdmin):
    list_display=['id','name','location','items']