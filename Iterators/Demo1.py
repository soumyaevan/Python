def my_Iterator(iterable,func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)
def square(x):
    print(x*x)            
        
my_Iterator([1,2,3,4,5],square)
my_Iterator("Hello",print)