def quantos_uns(n):
    numero = str(n)
    quantidade = []
    termos = len(numero)
    i = 0
    while i < (termos):
        if numero[i] == '1':
            quantidade.append(numero[i])
        i += 1
    return len(quantidade)
        