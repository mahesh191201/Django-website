from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
  
    title=models.CharField(max_length=255)
    timeStamp=models.DateTimeField(blank=True)
    content=RichTextField(blank=True, null=True)
    genre=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)

    def __str__(self):
        return self.title
