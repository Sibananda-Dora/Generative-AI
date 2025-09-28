#Daemon threads are background threads that automatically terminate when the main program or all non-daemon threads have finished their execution. This means that the Python interpreter will not wait for daemon threads to complete before exiting.


import threading
import time

def word():
    while True:
     print("Checking Spell\n")
     time.sleep(2)

t=threading.Thread(target=word) #daemon=True  
t.start()
print("Checking Done")