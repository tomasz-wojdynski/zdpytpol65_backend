from django.urls import path

from formsapp import views

app_name = 'formsapp'

urlpatterns = [
    path('1/', views.contact1, name='contact1'),
]