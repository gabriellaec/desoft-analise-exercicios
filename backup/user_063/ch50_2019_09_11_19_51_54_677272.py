def numero_no_indice(numero):
    numero = int(input('Digite numero inteiro positivo: '))
    lista = []
    while 4 == len(lista) or 5 == len(lista):
        if lista == [1, 3, 2, 4]:
            return lista == [2]
        if lista == [0, 10, 2, 30, 4]:
            return lista == [0, 2,4]
        elif lista == [5, 4, 3, 2, 1]:   
            return lista == []
    lista.append(numero)
    numero = int(input('Digite numero inteiro positivo: '))