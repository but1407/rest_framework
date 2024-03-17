from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.
class User(AbstractUser):
    avatar= models.ImageField(upload_to='uploads/%Y/%m')
    # username = models.CharField(max_length=100, unique=False, null=True, default=None)
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']


class Category(models.Model):
    name =models.CharField(max_length=255, null=False, unique=True)
    def __str__(self):
        return self.name
class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=255, null=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    image =models.ImageField(upload_to='courses/%Y/%m',default=None)
    

class Course(ItemBase):
    class Meta:
        unique_together  = ('subject','category')
        ordering = ["-id"]
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)    
    
    def __str__(self):
        return self.subject
    
class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject','course')
    content = RichTextField()
    course = models.ForeignKey(Course, related_name = "lessons",on_delete=models.CASCADE)    
    tags = models.ManyToManyField("Tag", blank=True, null=True )
    def __str__(self):
        return self.subject
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
