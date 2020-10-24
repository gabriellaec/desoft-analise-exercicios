def calcula_fibonacci(n):
    if n== 0:
        return []
    if n== 1:
        return [1]
    if n== 2:
        return [1,1]
    if n > 2:
        lista_fibonacci= [1,1]
        i= 2
        while i < n:
            lista_fibonacci.append(lista_fibonacci[i-1] + lista_fibonacci[i-2])
            i= i + 1
        return lista_fibonacci