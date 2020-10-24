def quantos_uns(numero):
    numero = str(numero)
    soma = 0
    n = 0
    while n<=numero:
        if numero[n] == '1':
            soma = soma + 1
        n = n + 1
    return soma