def customer():
    print("What would you like ?")
    order=yield
    while True:
        print(order)
        order=yield
stall=customer()
next(stall)
stall.send("mobile")
stall.send("laptop")