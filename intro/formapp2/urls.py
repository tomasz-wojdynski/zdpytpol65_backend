from django.urls import path

from formapp2 import views

app_name = 'formapp2'

urlpatterns = [
    path('', views.register, name='register')
]