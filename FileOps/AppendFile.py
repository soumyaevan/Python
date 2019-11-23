''' with open('C:\\Python_T\\Python\\FileOps\\fileWr1.txt','a') as file:
    file.write("Wow!!! Appended a new line\n") '''
    
with open('C:\\Python_T\\Python\\FileOps\\fileWr1.txt','r+') as file:
    text = file.read()
    newText = text.replace('row','line')
    #file.seek(0)
    file.write(newText)
    file.truncate()