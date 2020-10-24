numero=int(input('digite um numero:'))
while numero>0:
    numero=int(input('digite um numero:'))
    lista=[]
    lista.append(numero)
    if numero<=0:
        lista.reverse()
        print(lista)
