from django.db import models
 
class Todo(models.Model):

    name = models.CharField(max_length=100, unique=True) 
    description = models.TextField(max_length=200)
    created = models.DateTimeField() 
 
    def __str__(self): 
        return self.name