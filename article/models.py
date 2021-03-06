from django.db import models


class ArticleUser(models.Model):
    auth_user = models.OneToOneField(
        primary_key=True,
        to='auth.User',
        on_delete=models.CASCADE
    )
    is_blocked = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_enabled = models.BooleanField(default=True)
    is_visible_for_quests = models.BooleanField(default=True)
    include_in_menu = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_category = models.ForeignKey('self', blank=True, null=True, related_name='children')

    def get_choice(self):
        return self.id_category, str(self.name), self.id_category


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    unique_id_article = models.PositiveIntegerField(serialize=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    is_visible_for_quests = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_article = models.ForeignKey(null=True, to='article.Article')
    category = models.ForeignKey(Category, null=True)
    author = models.ForeignKey(ArticleUser, null=True)


class Comment(models.Model):
    id_model = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(ArticleUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


RATE_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
]


class Rating(models.Model):
    id_rating = models.AutoField(primary_key=True)
    rate = models.CharField(max_length=1, choices=RATE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)







