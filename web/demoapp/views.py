import random
from django.shortcuts import render
from . import tasks


def index(request):
    context = {}
    return render(request, 'demoapp/index.html', context)


def celery_index(request):
    context = {}
    return render(request, 'demoapp/celery_index.html', context)


def random_add(request):
    a, b = random.choices(range(100), k=2)
    tasks.add.delay(a, b)
    context = {'function_detail': 'add({}, {})'.format(a, b)}
    return render(request, 'demoapp/celery_detail.html', context)


def random_mul(request):
    a, b = random.choices(range(100), k=2)
    tasks.mul.delay(a, b)
    context = {'function_detail': 'mul({}, {})'.format(a, b)}
    return render(request, 'demoapp/celery_detail.html', context)


def random_xsum(request):
    array = random.choices(range(100), k=random.randint(1, 10))
    tasks.xsum.delay(array)
    context = {'function_detail': 'xsum({})'.format(array)}
    return render(request, 'demoapp/celery_detail.html', context)
