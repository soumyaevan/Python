def fileOperation():
    file = open('C:\\Python_T\\Python\\FileOps\\file1.txt')
    for line in file.readlines():
        print(line)
    if not file.closed:
        file.close()
        
def fileOPSWith():
    with open('C:\\Python_T\\Python\\FileOps\\file1.txt') as file:
        print(file.read())
         
fileOPSWith()