numeros = int(input('digite numeros inteiros: '))
lista = []
programa = True
while programa:
    if numeros <= 0:
        programa = False
    else:
        lista.append(numeros)
print(lista)
    
