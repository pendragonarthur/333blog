from django.db import models
from django.utils.text import slugify

class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Rascunho'),
        ('published', 'Publicado'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, editable=False)
    content = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, default=1)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True) 
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ['-posted_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    