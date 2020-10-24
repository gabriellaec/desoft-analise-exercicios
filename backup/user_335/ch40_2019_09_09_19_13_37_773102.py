def fatorial():
    n = int(input("Digite um número para calcular a fatorial: "))
    valor = 1
    while n!=1:
        valor *= n
        n = n-1
    return valor