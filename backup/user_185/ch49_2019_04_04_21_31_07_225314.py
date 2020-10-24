digite_positivos = int(input("Digite números positivos: "))
while digite_positivos >  0:
    lista.append(digite_positivos)
    digite_positivos = int(input("Digite números positivos: "))
print(lista[::-1])