from django import forms
from .models import Advertisement
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AdvertisementForm(forms.ModelForm):
    """
    Этот блок кода определяет метаданные (Meta) для модели Advertisement. model = Advertisement: Это указывает Django,
    что эти метаданные относятся к модели Advertisement. Это не обязательно нужно явно указывать, так как Django обычно
    может определить это автоматически.
    fields = ['title', 'content', 'author'] Это список полей модели, которые будут отображаться в форме модели. В
    данном случае это заголовок объявления (title), содержание (content) и автор (author).
    """
    class Meta:
        model = Advertisement
        fields = ['title', 'content', 'image', 'author']

class SignUpForm(UserCreationForm):
    """
    Этот класс SignUpForm представляет собой кастомную форму регистрации пользователя, которая расширяет стандартную
    форму UserCreationForm. UserCreationForm - Это стандартная форма Django для регистрации новых пользователей.
    SignUpForm расширяет UserCreationForm, что позволяет переопределить некоторые аспекты формы, если необходимо.
    Использование Meta позволяет задать метаданные формы без необходимости создавать отдельный экземпляр класса.
    Поле fields определяет, какие поля формы будут отображаться. В данном случае это базовые поля для регистрации
    пользователя.
    """
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
