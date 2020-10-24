lista = []
a = int(input("Numero:"))
lista.append(a)
i = 0
while i < len(lista):
    if a <= 0:
        break
    else:
        lista.append(a)
        a = int(input("Numero:"))
        i += 1


while i >= 0:
    print(lista[i])
    i -= 1