def verifica_lista(lista):
    lista_par = []
    lista_impar = []
    i = 0
    while i < len(lista):
        if lista[i]%2 == 0:
            lista_par.append(lista[i])
        else:
            lista_impar.append(lista[i])
        i += 1
    if len(lista_par) == len(lista):
        print('par')
    elif len(lista_impar) == len(lista):
        print('impar')
    else:
        print('misturado')