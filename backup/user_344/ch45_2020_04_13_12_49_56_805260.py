num = int(input('Digite numeros maiores que 0:'))
lista =[]
while num >0:
    lista.append(num)
    num = int(input('Digite numeros maiores que 0:'))
print (lista[::-1])
    
