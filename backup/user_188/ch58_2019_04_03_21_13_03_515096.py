def calcula_fibonacci(numero):
    lista_fibonacci = []
    lista_fibonacci.append(1)
    lista_fibonacci.append(1)
    contador = 2
    while contador < numero + 1:
        lista_fibonacci.append(lista_fibonacci[contador - 1] + lista_fibonacci[contador - 2])
        contador += 1
    return lista_fibonacci