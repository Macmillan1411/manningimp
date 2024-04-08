from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class BlogContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='content')
    ELEMENT_CHOICES = [
        ('heading', 'Заголовок'),
        ('paragraph', 'Абзац'),
        ('list', 'Список'),
        ('image', 'Картина'),
        # Add more choices as needed
    ]
    element_type = models.CharField(max_length=10, choices=ELEMENT_CHOICES)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='blog_images/', blank=True)
    
    def __str__(self):
        return f"Content {self.blog.title}-{self.element_type}"
