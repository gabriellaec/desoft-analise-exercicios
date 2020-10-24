lista1 = []
lista2 = []
exercicio = True
while exercicio:
    a = int(input('Qual o número? '))
    if a > 0:
        lista1.append(a)
    else:
        break
i = 1
if len(lista1) > 0:
    exercicio2 = True
    while exercicio2:
        lista2.append(lista1[len(lista1) - i])
        i += 1
        if len(lista1) == len(lista2):
            break
print(lista2)