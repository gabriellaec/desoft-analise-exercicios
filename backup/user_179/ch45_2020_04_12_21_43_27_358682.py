numero = int(input('n: '))
lista = []
lista.append(numero)
while numero > 0:
    numero = int(input('n: '))
    lista.append(numero)
    
a = lista.reverse()
print (a)