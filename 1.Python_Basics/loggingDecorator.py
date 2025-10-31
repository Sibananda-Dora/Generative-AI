from functools import wraps

def logActivity(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling: {func.__name__}")
        result= func(*args,**kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper
@logActivity
def brew(type,stat="ongoing"):
    print(f"Brewing {type} chai and Status {stat}")
brew("masala","finished")