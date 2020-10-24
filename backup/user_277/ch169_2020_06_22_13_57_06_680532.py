def login_disponivel(string, lista):
    k = False
    j = 0
    for i in range(len(lista)):
        if string == lista[i]:
            j = int(j) + 1
            k = True
        if string + str(j) == lista[i]:
            j = int(j) + 1
            k = True
    if k:
        string = string + str(j)
        return string
    else:
        return string
lista = []
while a != 'fim':
    a = input('digite o usuario:')
    b = login_disponivel(a, lista)
    lista.append(b)
for j in range(len(lista)):
    print(lista[j])