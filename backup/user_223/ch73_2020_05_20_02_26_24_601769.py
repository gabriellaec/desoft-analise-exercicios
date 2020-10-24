def remove_vogais(s):
    lista = list(s)
    for i in lista:
        if i == 'a' or 'e' or 'i' or 'o' or 'u':
            lista.remove(i)
    final = ''.join(lista)
    print(final)