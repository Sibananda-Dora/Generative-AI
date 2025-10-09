import threading
import time

def order():
    for i in range(1,4):
        print(f"Order placed #{i}")
        time.sleep(2)
def process():
    for i in range(1,4):
        print(f"Order Processing #{i}")
        time.sleep(3)

#thread creation
order_thread=threading.Thread(target=order)
process_thread=threading.Thread(target=process)

order_thread.start()
process_thread.start()

order_thread.join()
process_thread.join()
print("Order is Ready")
