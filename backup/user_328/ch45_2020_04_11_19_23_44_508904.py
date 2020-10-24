lista= []
y= True
while y:
    x= int(input('Digite algum número: '))
    if x>0:
        lista.append(x)
    elif x <= 0:
        y= False
        lista.reverse()
        print(lista)