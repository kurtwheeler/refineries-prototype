from celery import Celery

app = Celery('downloader', broker='pyamqp://guest@localhost//')

@app.task
def download():
    fileObject = open("/testDir/temp", "w")
    fileObject.write("hello")
    fileObject.close()
    return 0
