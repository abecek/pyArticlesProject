from pprint import pprint
from django import forms
from django.contrib.auth.models import User
from article.models import ArticleUser
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime


class RegistrationForm(UserCreationForm):
    #email = models.EmailField(required=True)

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