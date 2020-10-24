def quantos_uns(numero):
    string = str(numero)
    soma = 0
    n = 0
    if string[n] == '1':
        soma = soma + 1
        n = n+1
        return soma
        