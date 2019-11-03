''' def fibonacci(max_num):
    nums = []
    x = 0
    y = 1
    count = 0
    while count < max_num:
        nums.append(y)
        x,y = y,x+y
        count+=1
        
    for item in nums:
        print(item)
fibonacci(5) '''
 
        
def feb_gen(max_num):
    x = 0
    y = 1
    count = 0
    while count < max_num:
        x,y = y,x+y
        yield x
        count+=1
                
for item in feb_gen(15):
    print(item)
        
        
        
