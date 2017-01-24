from celery import Celery

app = Celery('tasks', broker='amqp://localhost//')
@app.task
def cal():
    print('hi')
