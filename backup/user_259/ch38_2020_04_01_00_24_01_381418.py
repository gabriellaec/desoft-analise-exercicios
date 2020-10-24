def quantos_uns(numero):
    numero = str(numero)
    contador = 0
    for i in numero:
        if i == 1:
            contador+=1
    return contador
        
    