import threading
import time

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(10_000_000):  # Reduced iterations for better performance
        with lock:
            counter += 1

start = time.time()

# Create multiple threads
threads = []
for _ in range(4):  # Example: 4 threads
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

end = time.time()
print(f"Final counter value: {counter}")
print(f"Time taken: {end - start:.2f} seconds")
