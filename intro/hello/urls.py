from django.urls import path

from hello import views


urlpatterns = [
    path('home/', views.home),
    path('adam/', views.adam),
    path('ewa/', views.ewa),
    path('greet/', views.greet),

    path('<name>/', views.hello),
    path('2/<name>/', views.hello2),
]
