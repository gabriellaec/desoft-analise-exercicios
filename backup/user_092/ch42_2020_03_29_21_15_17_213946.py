p = input('palavra')
i = 0
lista = []
while p != 'fim':
    lista[i] = p
    if p[0] == 'a':
        print (p)
    i += 1
    p = input('palavra')