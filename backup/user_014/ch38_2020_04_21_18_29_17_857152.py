def quantos_uns(n):
    contador = 0
    numero = int(input('Digite um número: '))
    n = 0
    for n in numero:
        if n == 1:
            contador += 1
        else:
            contador = 0
    return contador