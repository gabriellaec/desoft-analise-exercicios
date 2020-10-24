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
        positivo == True

i2 = len(lista) - 1  
while i2 >= 0:
    lista2.append(lista[i2])
    i2 -= 1
        
print(lista2)