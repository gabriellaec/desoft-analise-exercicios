def quantos_uns(numero):
    numero = str(numero)
    quantos_uns = []
    for i in numero:
        if i == 1:
            quantos_uns.append(i)
    return len(quantos_uns)
        
    