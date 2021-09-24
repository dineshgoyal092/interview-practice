# from celery import Celery
# import os
# import shutil
#
#
# DES_DIR = '/Users/dinesh.goyal/Documents/celery/files'
# SOURCE_DIR = '/Users/dinesh.goyal/Documents/celery/archives'
#
# app = Celery(
#     'celeryApp', backend='redis://localhost:6379', broker='redis://localhost:6379'
# )
#
#
# @app.task
# def move():
#     """
#         hello
#     """
#     print("inside move fn")
#     source_files = os.listdir(SOURCE_DIR)
#     print(source_files)
#     for f in source_files:
#         shutil.copy(f, DES_DIR)
#
#
# @app.task
# def list_file():
#     return os.listdir(DES_DIR)



from celery import Celery
import requests
# from celery.task import task

app = Celery('moveFile', broker='redis://localhost:6379/0')
# app.autodiscover_tasks()

@app.task
def fetch_url(url):
    resp = requests.get(url)
    print("url", resp.status_code)


def fetch_url1(url):
    resp = requests.get(url)
    print("url", resp.status_code)

def func(urls):
    for url in urls:
        fetch_url.delay(url)


if __name__ == "__main__":
    import time
    start = time.time()
    func(["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"])
    end = time.time()
    print(end - start)



# how to run this
# for worker -> celery -A moveFile worker --loglevel=INFO
# another terminal
# python moveFile.py
# run redis in seperate server

