# Generated by Django 4.2 on 2023-05-30 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_foodblog_blog_title_alter_foodblog_blogpost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='foodblog',
            new_name='FoodBlogModel',
        ),
    ]
