def quantos_uns(numero):
    termos = 0
    contador = 0
    while termos < len(numero):
        if numero[termos] == '1':
            contador = contador + 1
            termos = termos + 1
        else:
            termos = termos + 1
    return contador