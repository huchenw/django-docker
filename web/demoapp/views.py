import random
from django.http import HttpResponse
from .tasks import add, mul, xsum


def random_add(request):
    a, b = random.choices(range(100), k=2)
    add.delay(a, b)
    html = '<html><body>add({}, {}) is called by celery, \
            "docker-compose logs celery" for detail</body></html>'.format(a, b)
    return HttpResponse(html)


def random_mul(request):
    a, b = random.choices(range(100), k=2)
    mul.delay(a, b)
    html = '<html><body>mul({}, {}) is called by celery, \
            "docker-compose logs celery" for detail</body></html>'.format(a, b)
    return HttpResponse(html)


def random_xsum(request):
    array = random.choices(range(100), k=random.randint(1, 10))
    xsum.delay(array)
    html = '<html><body>xsum({}) is called by celery, \
            "docker-compose logs celery" for detail</body></html>'.format(array)
    return HttpResponse(html)


def celery_test(request):
    base_url = '{scheme}://{host}/celery/'.format(
        scheme=request.scheme, host=request.get_host()
    )
    html_template = '''
    <html>
        <body>
            <ul>
                <li><a href='{url_add}'>{url_add}</a></li>
                <li><a href='{url_mul}'>{url_mul}</a></li>
                <li><a href='{url_xsum}'>{url_xsum}</a></li>
            </ul>
        </body>
    </html>
    '''
    html = html_template.format(
        url_add=base_url + 'add',
        url_mul=base_url + 'mul',
        url_xsum=base_url + 'xsum',
    )
    return HttpResponse(html)
