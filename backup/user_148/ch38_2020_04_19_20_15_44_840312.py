def quantos_uns(n):
    lista = []
    a = str(n)
    i = 0
    while i<len(a):
        if a[i] == '1':
            lista.append(a[i])
        i += 1
        
    return len(lista)
