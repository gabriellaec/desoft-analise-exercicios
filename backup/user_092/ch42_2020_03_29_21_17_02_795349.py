p = input('palavra')
i = 0
lista = ['a']*10000
while p != 'fim':
    if p[0] == 'a':
        print (p)
    lista[i] = p
    i += 1
    p = input('palavra')