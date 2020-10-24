def quantos_uns(n):
    numero = str(n)
    i = 0
    quantidade = []
    termos = len(numero)
    while i < termos:
        if numero[i] == 1:
            quantidade.append(i)
        i += 1
    return len(quantidade)
            
        