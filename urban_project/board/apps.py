from django.apps import AppConfig


class BoardConfig(AppConfig):
    """
    Этот класс BoardConfig(AppConfig) определяет конфигурацию для Django приложения. name = "board": Указывает полное
    имя приложения в Django. Атрибут default_auto_field = 'django.db.models.BigAutoField' определяет тип поля для
    автоматически увеличивающихся первичных ключей в модели Django.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'
