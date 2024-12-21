from datetime import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Advertisement
from .forms import AdvertisementForm, UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from .models import Profile


def logout_view(request):
    """
    Этот метод выполняет выход пользователя из системы и перенаправляет его на домашнюю страницу.
    """

    logout(request)

    return redirect('home')

def signup(request):
    """
    Вызывает страницу для подписи объявлений.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/board')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def home(request):
    """
    Вызывает страницу home.html.
    """
    return render(request, 'home.html')

def advertisement_list(request):
    """
    Вызывает страницу advertisement_list.html.
    """
    advertisements = Advertisement.objects.all()
    return render(request, 'board/advertisement_list.html', {'advertisements': advertisements})

def advertisement_detail(request, pk):
    """
    Вызывает страницу advertisement_detail.html .
    """
    advertisement = Advertisement.objects.get(pk=pk)
    return render(request, 'board/advertisement_detail.html', {'advertisement': advertisement})

@login_required  # Проверяет регистрацию пользователя
def add_advertisement(request):
    """
    Этот метод считывает данные объектов из класса Advertisement, проверяет были ли запрос "POST", обрабатывает
    данные формы, если все поля заполнены полностью, корректны и содержат все необходимые данные. Затем, при
    обавлении данных, автоматически устанавливает автора как текущего авторизованного пользователя. Если запроса "POST"
    не было, то возвращаемся к предыдущей странице без изменений.
    """
    if request.method == "POST":
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.author = request.user
            advertisement.save()
            return redirect('board:advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'board/add_advertisement.html', {'form': form})

@login_required    # Проверяет регистрацию пользователя
def edit_advertisement(request, pk):
    """
    Этот метод считывает данные объектов из класса Advertisement, проверяет были ли запрос "POST", обрабатывает
    данные формы, если все поля заполнены полностью, корректны и содержат все необходимые данные. Затем, при
    редактировании, автоматически устанавливает автора как текущего авторизованного пользователя. Если запроса "POST"
    не было, то возвращаемся к предыдущей странице без изменений.
    :param request:
    :param pk:
    :return:
    """
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            img_obj = form.instance
            # Перенаправляет на страницу с сохраненными исправлениями.
            return redirect('board:advertisement_detail', pk=img_obj.pk)
    else:
        # вызов функции которая отобразит в браузере указанный шаблон с данными формы и объявления.
        form = AdvertisementForm(instance=advertisement)
    return render(request, 'board/edit_advertisement.html',
                  {'form': form, 'advertisement': advertisement})

@login_required
def delete_advertisement(request, pk):
    """
    Этот метод считывает данные объектов из класса Advertisement, проверяет были ли запрос "POST", после чего удаляет
    объявление и возвращается в окно объявления.
    :param request:
    :param pk:
    :return:
    """
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        advertisement.delete()
        return redirect('board:advertisement_list')
    else:
        None
    return render(request, 'board/delete_advertisement.html', {'advertisement': advertisement})

@login_required
def create_advertisement(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save()
            return redirect('board:advertisement_detail', pk=advertisement.pk)
    else:
        form = AdvertisementForm()
    return render(request, 'board/create_advertisement.html', {'form': form})

@login_required
def likes(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        advertisement.likes += 1
        advertisement.save()
        return redirect('board:advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'board/advertisement_list.html', {'advertisement': advertisement})

@login_required
def dislikes(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        advertisement.dislikes += 1
        advertisement.save()
        return redirect('board:advertisement_list')
    else:
        None
    return render(request, 'board/advertisement_list.html', {'advertisement': advertisement})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Этот метод определяет колличество входов каждого пользователя и сохраняет в базе данных
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.profile.total_visits += 1
    instance.profile.save()

