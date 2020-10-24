num = int(input('manda numero: '))
li = []
while num > 0:
    li.append(num)
    num = int(input('manda numero: '))
    
li = reversed(li)
for i in li:
    print (i)
    