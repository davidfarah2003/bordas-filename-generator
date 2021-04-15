import urllib.request
import urllib.error
import threading
import numpy as np
import os

with open("links.txt", 'r') as file:
    urls = []
    url_list = file.readlines()
    for url in url_list:
        if "\n" in url:
            url = url.rstrip("\n")
        urls.append(url)

def check_code(urls):
    for url in urls:
        try:
            r = urllib.request.urlopen(url)
            print(r.code, "success:", url)
            os._exit(0)

        except urllib.error.HTTPError as e:
            print(e.code, ":", url)


splitted = np.array_split(urls, 7)
for array in splitted:
    worker = threading.Thread(target=check_code, args=(array,))
    worker.start()

