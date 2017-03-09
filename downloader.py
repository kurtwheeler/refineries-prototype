from celery import Celery

app = Celery('downloader', backend='rpc://', broker='amqp://guest@localhost//')

@app.task
def download():
    print("hi")
    fileObject = open("/testDir/temp", "w")
    fileObject.write("hello")
    fileObject.close()
    print("hello")
    return 0

@app.task
def add(x, y):
    print("Wolololo")
    return x + y
