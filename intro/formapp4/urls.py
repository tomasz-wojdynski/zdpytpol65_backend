from django.urls import path

from formapp4 import views

app_name = 'formapp4'

urlpatterns = [
    path('', views.register, name='register')
]