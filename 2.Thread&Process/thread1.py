# import threading
from multiprocessing import Process
import time
import requests

def downlaod(url):
    print(f"Starting downlaod {url}")
    resp=requests.get(url)
    print(f"finished downlaod {url}, Size : {len(resp.content)}")

urls=[
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
    ]
if __name__=='__main__':
    start=time.time()
    Processes=[]
    for url in urls :
        t=Process(target=downlaod,args=(url, ))
        t.start()
        Processes.append(t)
    for url in urls:
        t.join()
    end=time.time()

    print(f"Total Execution time: {end-start:.2f}")