from django.urls import path

from randomthought.views import thought

app_name = 'randomthought'

urlpatterns = [
    path('', thought, name='thought'),
    path('thought/', thought),
]