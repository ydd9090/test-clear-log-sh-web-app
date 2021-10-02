from wsgiref.simple_server import make_server
from loguru import logger
logger.add('info-{time:YYYY-MM-DD}.log', level='INFO', encoding='utf-8')
logger.add('warn-{time:YYYY-MM-DD}.log', level='WARNING', encoding='utf-8')


def log_it(func):
    count_map = {"count": 0}

    def wrapper(*args, **kwargs):
        func_return = func(*args, **kwargs)
        count_map['count'] = count_map['count']+1
        count = count_map['count']
        if count % 10 == 0:
            logger.warning('第{}次请求'.format(count))
        else:
            logger.info("第{}次请求".format(count))
        logger.info('Response body bytes:{}'.format(func_return))
        return func_return
    return wrapper


@log_it
def run(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello,world</h1>'
    return [body.encode('utf-8')]


if __name__ == '__main__':
    httpd = make_server('', 8000, run)
    logger.info('start server,listen on 8000...')
    httpd.serve_forever()
