def calcula_fibonacci(n):
    lista = [1, 1]
    i = 2
    while len(lista) < n:
        novo_termo = lista[i-1]+ lista[i-2]
        lista.append(novo_termo)
        i += 1
    return lista