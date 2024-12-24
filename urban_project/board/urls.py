from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import UpdateProfileStats

app_name = 'board'
urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('add/', views.add_advertisement, name='add_advertisement'),
    path('edit/<int:pk>/', views.edit_advertisement, name='edit_advertisement'),
    path('delete/<int:pk>/', views.delete_advertisement, name='delete_advertisement'),
    path('likes/<int:pk>/', views.likes, name='likes'),
    path('dislikes/<int:pk>/', views.dislikes, name='dislikes'),
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
