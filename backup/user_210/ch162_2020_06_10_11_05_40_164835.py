def verifica_lista(num):
    lista = []
    for each in num:
        if each % 2 == 0:
            lista.append(0)
        else:
            lista.append(1)
    if sum(lista) == 0 and len(lista)!= 0:
        return "par"
    elif sum(lista) == len(lista):
        return 'ímpar'
    else:
        return "misturado"
    