def remove_vogais(s):
    lista = list(s)
    i = 0
    for i in range (len(lista)-1):
        if lista[i] == 'a' or 'e' or 'i' or 'o' or 'u':
            del lista[i]
            i+=1
    final = ''.join(lista)
    print(final)