from django.urls import path

from formapp import views

app_name = 'formapp'

urlpatterns = [
    path('', views.register, name='register'),
]