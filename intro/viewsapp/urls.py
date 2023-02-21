from django.urls import path
from django.views.generic import TemplateView

from viewsapp import views

app_name = 'viewsapp'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),
    path('hello3/', views.HelloTemplateView.as_view(), name='hello3'),
    path('hello4/', views.TemplateView.as_view(template_name='viewsapp/hello.html'), name='hello4'),
]
