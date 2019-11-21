from functools import wraps
def log_Function_Data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"You are about to call {fn.__name__}")
        print(f"This function is about: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_Function_Data
def add(x,y):
    """Adding Numbers"""
    return x+y

print(add(5,6))