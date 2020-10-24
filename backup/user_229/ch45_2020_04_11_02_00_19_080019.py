positivo = True
lista = []
lista2 = []
while positivo == True:
    valor = int(input("Digite um  número positivo: "))
    if valor <= 0:
        positivo = False
        break
    else:
        lista.append(valor)
i = 0
i2 = len(lista)   
while i2 >= 0:
    lista2[i2] = lista[i]
    i += 1
    i2 -= 1
        
print(lista2)