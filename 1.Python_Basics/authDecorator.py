from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role !="admin":
            print("Access Denied!!")
        else:
            return func(user_role)
    return wrapper
        
@require_admin
def permission(role):
    print("Access Granted")

permission("user")
permission("admin")
