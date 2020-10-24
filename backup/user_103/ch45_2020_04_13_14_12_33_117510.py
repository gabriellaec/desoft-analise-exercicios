numero=int(input('digite um numero:'))
lista=[]
if numero>0:
    lista.append(numero)
while numero>0:
    numero=int(input('digite um numero:'))
    if numero<=0:
        break
    lista.append(numero)
lista.reverse()
print(lista)