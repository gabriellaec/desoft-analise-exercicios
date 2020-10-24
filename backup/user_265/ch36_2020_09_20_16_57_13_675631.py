a = int(input('n: '))
def fatorial(a):
    resultado = 1
    i = 1
    while i <= a:
        resultado *= i
        i += resultado
    return resultado
