def calcula_fibonacci(n):
    lista = [1, 1]
    if n == 1:
        return [1]
    while len(lista) < n:
        x = lista[-1] + lista[-2]
        lista.append(x)
    return lista
      
       