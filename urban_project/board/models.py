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
    image = models.ImageField(upload_to='advertisements/', blank=True, null=True)
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    dislikes = models.IntegerField(default=0, verbose_name='Дизлайки')

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
    image = models.ImageField(upload_to='advertisements/', blank=True, null=True)

    def __str__(self):
        """
        Метод используется для определения строкового представления объекта модели
        :return:
        """
        return f'Comment by {self.author} on {self.advertisement}'


from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Статистика
    total_visits = models.IntegerField(default=0)
    last_visit = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return f'Profile for {self.user}'

