from django.db import models
from django.contrib.auth.models import User

class Advertisement(models.Model):
    """
    Этот класс определяет модель для хранения информации об объявлениях в базе данных.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Метод используется для определения строкового представления объекта модели
        :return:
        """
        return self.title

class Comment(models.Model):
    """
    Этот класс определяет модель для хранения комментариев к статьям или другим объектам в базе данных.
    """
    advertisement = models.ForeignKey(Advertisement, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Метод используется для определения строкового представления объекта модели
        :return:
        """
        return f'Comment by {self.author} on {self.advertisement}'
