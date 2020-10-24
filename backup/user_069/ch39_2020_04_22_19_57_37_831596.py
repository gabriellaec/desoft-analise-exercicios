lista_termos = []
for i in range(1, 999):
    n = i
    lista = [0]
    lista[0] = n
    while n != 1:
        if n%2 == 0:
            n = n/2
            lista.append(n)
        else:
            n = 3*n + 1
            lista.append(n)
    lista_termos.append(lista)
t = 0
n = 0
for lista in lista_termos:
    if len(lista) > t:
        t = len(lista)
        n = lista[0]
print(n)