digite_positivos = int(input("Digite números positivos: "))
while True:
    if digite_positivos >=  0:
        lista.append(digite_positivos)
        digite_positivos = int(input("Digite números positivos: "))
    else:
        break
print(lista[::-1])