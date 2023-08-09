from django.contrib import admin
class Blog_Admin(admin.ModelAdmin):
    list_display = ('id','blog_title','author','blogpost')
    #list_display = ('blog_title','author')
    search_fields = ('blog_title','author')
    #search_fields = ('blog_title',)
    list_filter = ('blog_title','author')
    #list_filter = ('blog_title',)
    ordering = ('id',)
# Register your models here.
from .models import FoodBlogModel
admin.site.register(FoodBlogModel,Blog_Admin)
