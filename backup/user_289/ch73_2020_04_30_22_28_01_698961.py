def remove_vogais(string):
    lista = []
    for elemento in string:
        lista.append(elemento)
    e = 0
    while e < len(lista):
        if lista[e] == 'a' or 'e' or 'i' or 'o' or 'u':
            del lista[e]
            e += 1
        else:
            e += 1
    if len(lista) > 0:
        string_sem_vogal = ''.join(lista)
    else:
        string_sem_vogal = ''
    return string_sem_vogal
            