from django.urls import path

from stateapp import views

app_name = 'stateapp'

urlpatterns = [
    path('set-cookie/', views.set_cookie, name='set-cookie'),
    path('show-cookies/', views.show_cookies, name='show-cookies'),
    path('delete-cookie/', views.delete_cookie, name='delete-cookie'),
]
