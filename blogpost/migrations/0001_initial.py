# Generated by Django 4.2 on 2023-05-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='foodblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogpost', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
            ],
        ),
    ]
