from django.urls import path

from viewsapp import views

app_name = 'viewsapp'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),

]
