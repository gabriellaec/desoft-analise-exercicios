lista = []
i = 0
while i <= len(lista):
    a = int(input("Numero:"))
    if a <= 0:
        break
    else:
        lista.append(a)
        i += 1


while i >= 0:
    print(lista[i])
    i -= 1
