def calcula_fibonacci(n):
    lista = []
    soma = 2
    while len(lista) < n:
        if len(lista) < 2:
            lista.append(1)
        else:
            size = len(lista)
            soma = lista[size-1] + lista[size-2]
            lista.append(soma)
    return lista
        
        