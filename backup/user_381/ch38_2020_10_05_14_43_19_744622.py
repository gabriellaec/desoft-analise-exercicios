def quantos_uns(n):
    numero = str(n)
    i = 0
    termos = len(numero)
    while i < termos:
        if numero[i] == 1:
            numero.count(1)
        i += 1
    return numero.count(1)
            
        