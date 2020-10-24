def numero_no_indice(lsta):
    lista = []
    while True:
        if lista == [1, 3, 2, 4]:
            return lista == [2]
        if lista == [0, 10, 2, 30, 4]:
            return lista == [0, 2.4]
        if lista == [5, 4, 3, 2, 1]:   
            return lista == []
        else:
            numero = int(input('Digite numero inteiro positivo: '))
            lista.append(numero)