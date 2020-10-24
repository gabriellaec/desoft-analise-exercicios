def remove_vogais(n):
    i = 0
    lista_nova = []
    while i < len(n):
        if n[i] != 'a' and n[i] != 'e' and n[i] != 'i' and n[i] != 'o' and n[i] !='u':
            lista_nova.append(n[i])
        i += 1
    m = ''.join(lista_nova)
    return m