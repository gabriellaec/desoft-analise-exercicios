p = str(input('palavra'))
i = 0
lista = ['a']*10000
while p != 'fim':
    if p[0] == 'a':
        print (p)
    lista.append(p)
    p = str(input('palavra'))