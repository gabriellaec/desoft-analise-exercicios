def quantos_uns (n):
    lista = []
    i = 0
    while i <= len(n):
        if n[i] == 1:
            lista.append (n)
    return len(lista)