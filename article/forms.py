from pprint import pprint
from django import forms
from django.contrib.auth.models import User
from article.models import ArticleUser, Article, Category
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from datetime import datetime


class ArticleForm(forms.ModelForm):
    category_choices = []
    category = forms.Select(choices=category_choices)

    def __init__(self, *args, **kwargs):
        categories = Category.objects.all()
        for cat in categories:
            self.category_choices.append((str(cat.id_category), str(cat.name)))
        super(ArticleForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Article
        fields = {
            'unique_id_article',
            'title',
            'content',
            'is_published',
            'is_visible_for_quests',
            'parent_article',
            'category'
        }

    def save(self, commit=True):
        article = super(ArticleForm, self).save(commit=True)
        article.unique_id_article = self.cleaned_data.get('unique_id_article')
        article.title = self.cleaned_data.get('title')
        article.content = self.cleaned_data.get('content')
        article.is_published = self.cleaned_data.get('is_published')
        article.is_visible_for_quests = self.cleaned_data.get('is_visible_for_quests')
        article.parent_article = self.cleaned_data.get('parent_article')
        article.category = self.cleaned_data.get('category')

        if commit:
            article.save()

        return article


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        }

    def save(self, commit=True):
        authUser = super(RegistrationForm, self).save(commit=True)
        authUser.first_name = self.cleaned_data.get('first_name')
        authUser.last_name = self.cleaned_data.get('last_name')
        authUser.email = self.cleaned_data.get('email')

        articleUser = ArticleUser()

        if commit:
            articleUser.auth_user = authUser
            articleUser.updated_at = datetime.now()
            articleUser.is_blocked = False

            authUser.save()
            articleUser.save()

        return authUser


class ChangePasswordForm(PasswordChangeForm):

    class Meta :
        model = User
        fields = {
            'new_password1',
            'new_password2',
            'old_password'
        }

    def save(self, commit=True):
        authUser = super(ChangePasswordForm, self).save(commit=True)
        authUser.password = self.cleaned_data.get('new_password1')

        if commit:
            authUser.save()

        return authUser