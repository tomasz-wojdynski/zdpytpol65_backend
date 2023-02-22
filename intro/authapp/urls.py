from django.urls import path

from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
]