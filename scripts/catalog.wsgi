def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!  You have reached a1site.scripts.catalog.wsgi'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]