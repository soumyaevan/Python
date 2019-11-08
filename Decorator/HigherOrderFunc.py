def sum(num,func):
    x = 0
    for i in range(num):
        x += func(i)
        
    return x
        
def square(n):
    return n * n
def cube(n):
    return n * n * n

print(sum(3,cube))