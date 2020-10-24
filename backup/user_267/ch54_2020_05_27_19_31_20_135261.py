f1 = 1
f2 = 1
lista = []
def calcula_fibonacci(n):
    i = 3
    while i <= n:
        fe = [i-1]+[i-2]
        lista.append(fe)
    i += 1
    return lista
    