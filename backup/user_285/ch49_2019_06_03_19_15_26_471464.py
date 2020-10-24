num = int(input('manda numero: '))
li = []
while num >= 0:
    li.append(num)
    num = int(input('manda numero: '))
    
for i in range(len(li)):
    print (li[len(li)-i+1])
    