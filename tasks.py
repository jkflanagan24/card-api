from celery import Celery
from urllib.parse import quote

app = Celery(
    "tasks",
    broker="amqp://guest@localhost//",
    backend="rpc://"
)


@app.task
def add(x, y):
    return x + y
