from multiprocessing import Process
import time
def brew():
    print(f"started ...")
    count=1
    for _ in range(100_000_000):
        count+=1
    print(f"finished ...")
if __name__=='__main__':
    start=time.time()
    p1=Process(target=brew)
    p2=Process(target=brew)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end=time.time()
    print(f"time taken :{end-start:.2f}")

