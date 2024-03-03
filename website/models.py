from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length = 255)
    messsagw = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    upated_date = models.DateTimeField(auto_now= True)
    
    class Meta:
        ordering = ['created_date']
        
    def __str__(self) -> str:
        return self.name
    
    