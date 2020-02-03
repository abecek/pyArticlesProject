from django.db import models
from datetime import datetime


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=75)
    email = models.CharField(max_length=50)


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateField(datetime.now())
    content = models.TextField()


class Comment(models.Model):
    id_model = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(datetime.now())
    updated_at = models.DateField(null=True)
    content = models.TextField()


