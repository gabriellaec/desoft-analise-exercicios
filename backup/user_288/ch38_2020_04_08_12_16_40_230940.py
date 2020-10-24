def quantos_uns (n):
    lista = []
    i = 0
    n = str (n)
    while i < len(n):
        if n[i] == '1':
            lista.append (n)
        i += 1
    return len(lista)