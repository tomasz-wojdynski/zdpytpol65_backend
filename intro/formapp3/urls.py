from django.urls import path

from formapp3 import views

app_name = 'formapp3'

urlpatterns = [
    path('', views.register, name='register')
]