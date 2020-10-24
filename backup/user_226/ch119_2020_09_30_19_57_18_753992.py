def fatorial(n):
    i = n - 1
    resultado = n
    if n == 0:
        return 1
    else:
        while i > 0:
            resultado = resultado * 1
            i -= 1
        return resultado

def calcula_euler(x, n):
    lista = []
    i = 0
    while i < n:
        lista.append(x ** i/ fatorial(i))
        i += 1
    return sum(lista)