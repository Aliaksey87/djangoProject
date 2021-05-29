"""

Список urlpatterns направляет URL-адреса в представления. Для получения дополнительной информации см .:
     https://docs.djangoproject.com/en/3.2/topics/http/urls/
Примеры:
Представления функций
     1. Добавьте импорт: из представлений импорта my_app
     2. Добавьте URL-адрес в urlpatterns: path ('', views.home, name = 'home')
Представления на основе классов
     1. Добавьте импорт: from other_app.views import Home
     2. Добавьте URL-адрес в urlpatterns: path ('', Home.as_view (), name = 'home')
Включение другого URLconf
     1. Импортируйте функцию include (): из импорта django.urls include, path
     2. Добавьте URL-адрес в urlpatterns: path ('blog /', include ('blog.urls'))
"""
# Конфигурация URL-адреса djangoProject
#
# Список urlpatterns направляет URL-адреса в представления. Для получения дополнительной информации см .:
#      https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Примеры:
# Представления функций
#      1. Добавьте импорт: из представлений импорта my_app
#      2. Добавьте URL-адрес в urlpatterns: path ('', views.home, name = 'home')
# Представления на основе классов
#      1. Добавьте импорт: from other_app.views import Home
#      2. Добавьте URL-адрес в urlpatterns: path ('', Home.as_view (), name = 'home')
# Включение другого URLconf
#      1. Импортируйте функцию include (): из импорта django.urls include, path
#      2. Добавьте URL-адрес в urlpatterns: path ('blog /', include ('blog.urls'))

from django.urls import path
from app.views import index
from app.views import *

urlpatterns = [
    path('main_page', index),
    path('page2', index2),
    path('page3', page3),
    path('name', name),
    path('start_page', start_page),
    path('parol', login_user),
    path('log_out', do_logout),
    path('register', register),
    path('showregister', register2),
    path('', index)
]
