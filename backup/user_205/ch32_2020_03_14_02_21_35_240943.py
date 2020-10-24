def lista_primos(numero):
    lista = [2, ] 
    div = 3
    while numero > div:
        div+=2
        if (numero % div == 0):
            return False
        else:
            lista.append (div)