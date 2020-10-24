def calcula_fibonacci(numero):
    lista_fibonacci = [0] * numero
    lista_fibonacci[0] = 1
    lista_fibonacci[1] = 1
    contador = 2
    while contador < numero:
        lista_fibonacci[contador] = lista_fibonacci[contador - 1] + lista_fibonacci[contador - 2]
        contador += 1
    return lista_fibonacci