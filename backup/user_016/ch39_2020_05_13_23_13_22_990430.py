dicionario = {}
i = 1
for n in range (1,1000): 
    lista = []
    while n != 1:
        if n%2 == 0:
            n = n/2
            lista.append(n)
        else:
            n = 3*n + 1
            lista.append(n)
    dicionario[i] = len(lista)
    i += 1
a = max(dicionario.values())
for g in dicionario.keys():
    if dicionario[g] == a:
        print(g)