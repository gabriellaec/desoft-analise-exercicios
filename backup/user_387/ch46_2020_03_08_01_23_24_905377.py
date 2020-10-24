def numero_no_indice(a):

    lista = []

    for num in a:

        if num == a.index(num):
            lista.append(num)

    return(lista)