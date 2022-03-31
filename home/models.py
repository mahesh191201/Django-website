from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    content=models.TextField()
    answer=models.CharField(max_length=2)

    def __str__(self):
      return 'Message from '+ self.name + ' - ' + self.email 
    