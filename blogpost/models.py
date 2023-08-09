from django.db import models

# Create your models here.
class FoodBlogModel(models.Model):
    blog_title = models.CharField(max_length=100,default="not defined")
    blogpost = models.TextField()
    author =models.CharField(max_length=20)
    
    # def __str__(self):
    #     #return self.blog_title
    #     return f"{self.blog_title} by {self.author}"