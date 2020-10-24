lista=[]
numero=int(input('numero: '))
while numero>0:
    lista=lista.append(numero)
    numero=int(input('numero: '))
    if numero<=0:
        print(lista.reverse())