from django.db import models

# Create your models here.


class Post(models.Model):
    # image = 
    # tag = 
    # author = 
    # category = 
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.IntegerField(default = 0)
    status = models.BooleanField()
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    upated_date = models.DateTimeField(auto_now= True)    
    
    def __str__(self) -> str:
        return f"{self.title}: for id: {self.id}"