def sum(func):
    def do_Sum(num):
        x = 0
        for i in range(num):
            x += func(i)
        print(x)        
    return do_Sum
@sum        
def square(n):
    return n * n

@sum
def cube(n):
    return n * n * n

cube(3)
square(3)