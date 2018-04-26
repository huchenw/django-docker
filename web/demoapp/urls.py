from django.urls import path
from . import views

app_name = 'demoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('celery/', views.celery_index, name='celery_index'),
    path('celery/random_add/', views.random_add, name='celery_random_add'),
    path('celery/random_mul/', views.random_mul, name='celery_random_mul'),
    path('celery/random_xsum/', views.random_xsum, name='celery_random_xsum'),
]
