def verifica_progressao(lista):
    if lista[1] - lista[0] == lista[2] - lista[1]:
        return "PA"
    elif lista[1] / lista[0] == lista[2] / lista[1]:
        return "PG"
    else:
        return "NA"