def numero_no_indice(numero):
    lista = []
    while True:
        if lista == [1, 3, 2, 4]:
            lista.append(numero)
            return lista == [2]
        if lista == [0, 10, 2, 30, 4]:
            lista.append(numero)
            return lista == [0, 2.4]
        elif lista == [5, 4, 3, 2, 1]:   
            lista.append(numero)
            return lista == []
    numero = float(input('Digite numero inteiro positivo: '))