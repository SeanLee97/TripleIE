# config.py
import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing

# debug = True
bind = "0.0.0.0:8080"
pidfile = "log/gunicorn.pid"
accesslog = "log/access.log"
errorlog = "log/error.log"
loglevel = 'error'

# 开启后台运行，默认为False
daemon = True

# 启动的进程数 workers是工作进程数量，取的是CPU的数量
workers = multiprocessing.cpu_count()
# worker_class是指开启的每个工作进程的模式类型，默认为sync模式，也可使用gevent模式
worker_class = 'gevent'

x_forwarded_for_header = 'X-FORWARDED-FOR'

# 超过这么多秒后工作将被杀掉，并重新启动。一般设定为30秒
timeout = 30

# 在keep-alive连接上等待请求的秒数，默认情况下值为2。一般设定在1~5秒之间。
keepalive = 30
