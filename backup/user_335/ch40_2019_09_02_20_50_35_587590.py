def fatorial():
    x = int(input("Digite um número para calcular a fatorial: "))
    valor = 1
    while x!=1:
        valor *= x
        x = x-1
    return valor