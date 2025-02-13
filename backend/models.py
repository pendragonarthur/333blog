from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True) 
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)  
    def __str__(self):
        return self.title