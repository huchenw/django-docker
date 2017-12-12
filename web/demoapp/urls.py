from django.urls import path
from .views import *

urlpatterns = [
    path('', celery_test),
    path('add/', random_add),
    path('mul/', random_mul),
    path('xsum/', random_xsum),
]
