from django.urls import path

from formsapp import views

app_name = 'formsapp'

urlpatterns = [
    path('1/', views.contact1, name='contact1'),
    path('2/', views.contact2, name='contact2'),
    path('3/', views.contact3, name='contact3'),
]