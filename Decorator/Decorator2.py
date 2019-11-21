def upper(fn):
    def wrapper(*args):
        return fn(*args).upper()
    return wrapper

@upper
def greet(name):
    return f"Hi! My name is {name}"
@upper
def order(main, side):
    return f"Please bring one {main} with {side}"
@upper
def shout():
    return "Quick!!!"

print(greet("Soumya"))
print(order("Pizza","Coke"))
print(shout())