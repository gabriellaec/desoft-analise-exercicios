def quantos_uns(numero):
    soma = 0
    n = 0
    numerostr=str(numero)
    while n < len(numerostr):
        if numerostr[n] == "1":
            soma = soma + 1
            n = n + 1
            
        else:
            pass
    return soma

