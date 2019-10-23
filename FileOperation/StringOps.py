def getLastChar(num):
    num1 = str(num)
    return num1[-1:]

def getReverse(num):
    num1 = str(num)
    num1 = num1[::-1]
    return num1

print(getReverse('37582588x'))
print(getReverse(37582588))
print(getReverse('375825&88x'))