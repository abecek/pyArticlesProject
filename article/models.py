from django.db import models
from datetime import datetime


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=75)
    email = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(datetime.now())
    updated_at = models.DateField(null=True)
    last_login_at = models.DateField(null=True)
    is_blocked = models.BooleanField(default=False)
    auth_user = models.ForeignKey(null=True, to='auth.User', on_delete=models.CASCADE)


class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    description = models.TextField()
    is_enabled = models.BooleanField(default=True)
    is_visible_for_quests = models.BooleanField(default=True)
    include_in_menu = models.BooleanField(default=True)
    parent_category = models.ForeignKey(null=True, to='article.Category')


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    unique_id_article = models.PositiveIntegerField(serialize=False)
    title = models.CharField(max_length=200)
    created_at = models.DateField(datetime.now())
    updated_at = models.DateField(null=True)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    is_visible_for_quests = models.BooleanField(default=True)
    parent_article = models.ForeignKey(null=True, to='article.Article')
    category = models.ForeignKey(Category, null=True)
    author = models.ForeignKey(User, null=True)


class Comment(models.Model):
    id_model = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateField(datetime.now())
    updated_at = models.DateField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class Rating(models.Model):
    id_rating = models.AutoField(primary_key=True)
    rate = models.IntegerField()







