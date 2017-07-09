# _*_ coding: utf-8 _*_
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Answer
from .models import Code
from django.forms import TextInput, Textarea

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        labels = {'username' : 'Nazwa użytkownika',
                  'email' : 'Email',
                  'password1' : 'Hasło',
                  'password2' : 'Powtórz hasło',
                  }
        help_texts = {
            'username' : '',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('prize','answer_text',)
        labels = {
            'prize' : 'Wybierz nagrodę',
            'answer_text' : 'Twoja odpowiedź',
        }
        widgets = {
            'answer_text': Textarea(attrs={'class':'form-control', 'style':'height: 100px'}),
        }


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ('code',)
        labels = {
            'code' : 'Wpisz otrzymany kod',
        }

