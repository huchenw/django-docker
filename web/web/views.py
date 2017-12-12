from django.http import HttpResponse


def index(request):
    base_url = '{scheme}://{host}/'.format(
        scheme=request.scheme, host=request.get_host()
    )
    html_template = '''
    <html>
        <body>
            <ul>
                <li><a href='{url_admin}'>{url_admin}</a></li>
                <li><a href='{url_celery}'>{url_celery}</a></li>
            </ul>
        </body>
    </html>
    '''
    html = html_template.format(
        url_admin=base_url + 'admin',
        url_celery=base_url + 'celery'
    )
    return HttpResponse(html)
