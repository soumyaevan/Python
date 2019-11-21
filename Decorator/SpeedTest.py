from time import time
from functools import wraps
def speedTest(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Elapssed time of {fn.__name__} is {end_time - start_time}")
        return result
    return wrapper


@speedTest
def sum_gen(num):
    return sum(x for x in range(num))

@speedTest
def sum_list(num):
    return sum([x for x in range(num)])

print(sum_gen(90000000))
print(sum_list(90000000))

