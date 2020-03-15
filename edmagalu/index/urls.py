from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='menu'),
    path('login',views.login, name='login')
]