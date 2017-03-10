import requests
import sys
import os

from celery import Celery

app = Celery('downloader', broker='pyamqp://guest@localhost//')

@app.task
def download(url):
    target_folder = "/testDir/"
    filename = url.split('/')[-1]
    target_filename = target_folder + '/' + filename
    target_file = open(target_filename, "w")

    download_request = requests.get(url, stream=True)

    # chunk_size is in bytes
    for chunk in download_request.iter_content(chunk_size=4096):
        if chunk:
            target_file.write(chunk)
            target_file.flush()

    target_file.close()

def write_file():
    fileObject = open("/testDir/temp", "w")
    fileObject.write("hello")
    fileObject.close()
    return 0
