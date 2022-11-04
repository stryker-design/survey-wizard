from django.db import models
from django .contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid

# Create your models here.




class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = RichTextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

