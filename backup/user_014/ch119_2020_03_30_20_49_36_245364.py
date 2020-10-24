def fatorial (n):
    resultado = 1
    conta = 1
    while conta <= n:
        resultado *= conta
        conta += 1

def calcular_euler(x,n):
    i = 1
    contador = 1
    while i < n:
        contador = contador + (x**i)/ fatorial(i)
        i += 1
    return contador
    