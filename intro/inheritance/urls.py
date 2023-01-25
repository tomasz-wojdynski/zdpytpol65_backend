from django.urls import path

from inheritance import views

urlpatterns = [
    path('first/', views.first),
    path('second/', views.second),
]
