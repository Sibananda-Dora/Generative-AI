def infinite():
    count = 1
    while True:
        yield f"refill #{count}"
        count+=1
c= infinite()
for _ in range(6):
    print(next(c))