from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    recipe_yield = models.CharField(max_length=200)
    #this will need to be a class so it can say x servings, or y people or whatever
    #photo
    #cook time
    #comments
    #ingredients
    #preparation
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

''' Using char fields for now until I better understand relationships '''
class Cookbook(models.Model):
    owner = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    members = models.CharField(max_length=200) #people who contributed
    membership = models.CharField(max_length=200) #access group
    
class Member(models.Model):
    name = models.CharField(max_length=200)
    memberships = models.CharField(max_length=200)
    # there probably is something around a User here. a user will be a member and have memberships
    
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    INGREDIENT_TYPES = (
        ('D', 'Dry'),
        ('W', 'Wet'),
    )
    
    type = models.CharField(blank=True, choices=INGREDIENT_TYPES, max_length=5)
    
class Preparation(models.Model):
    pass
    
class Size(models.Model):
    pass
 
    
