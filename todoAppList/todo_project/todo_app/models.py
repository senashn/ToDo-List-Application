from django.db import models
from datetime import datetime
# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,blank=True)
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now ,blank=True )

    def __str__(self):
        return self.title
    


