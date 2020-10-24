def quantos_uns(numero):
    string = str(numero)
    soma = 0
    n = 0
    while n<=len(string):
        if string[n] == '1':
            soma = soma + 1
            n = n+1
    return soma
        