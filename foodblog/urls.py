"""
URL configuration for foodblog project.

The `urlpatterns` list routes URLs to blogview. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', blogview.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogpost import views as blogview
# from blogpost import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogview.bloghome),
    path('shake/', blogview.blogshake),
    path('profile/', blogview.blogprofile),
    path('travelblog/', blogview.travelblog),
    path('index2/', blogview.index2),
    path('blogs/', blogview.getAllBlogs),
    path('myform/', blogview.formView),
    path('blogform/', blogview.blogFormSubmit),
    path('myform/success/', blogview.successView),
    path('studentForm/', blogview.stdForm),
]
