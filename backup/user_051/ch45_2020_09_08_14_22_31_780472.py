lista=[]
while True:
    numero=int(input('Numero inteiro: '))
    if numero > 0:
        lista.append(numero)
    else:
        break
lista.reverse()
for numero in lista:
    print(numero)