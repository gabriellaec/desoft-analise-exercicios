lista = []
exercício = True
while exercício:
    a = int(input('Qual o número? '))
    if a != 0:
        lista.append(a)
    else:
        break
print(sum(lista))