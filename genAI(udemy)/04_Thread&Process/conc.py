import threading
import time

def brew():
    print(f"{threading.current_thread().name}started ...")
    count=1
    for _ in range(100_000_000):
        count+=1
    print(f"{threading.current_thread().name}finished ...")

thread1= threading.Thread(target=brew,name="brew1")
thread2=threading.Thread(target=brew,name="brew2")

start=time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end=time.time()
print(f"time taken :{end-start:.2f}")
