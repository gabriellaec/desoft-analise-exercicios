def simplifica_dict(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = ['a' ,'b', 'c', 'b', 'b', 'a']

lista = simplifica_dict(lista)
print (lista)

