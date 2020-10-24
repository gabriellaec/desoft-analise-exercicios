lista_termos = []
for n in range(1, 999):
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
maior_lista = max(lista_termos)
print(maior_lista[0])