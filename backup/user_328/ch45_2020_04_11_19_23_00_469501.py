lista= []
while True:
    x= int(input('Digite algum número: '))
    if x>0:
        lista.append(x)
    elif x <= 0:
        lista.reverse()
        print(lista)