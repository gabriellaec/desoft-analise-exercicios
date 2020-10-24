def quantos_uns(numero):
    numero = str(numero)
    contador = []
    for i in numero:
        if i == 1:
            contador.append(i)
    return len(contador)
        
    