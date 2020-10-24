def verifica_progressao(lista):
    if len(lista) == 0:
        return False
    for i in range(1, len(lista)-1):
        razaopa = lista[1] - lista[0]
        razaopg = lista[1]/lista[0]
        if (lista[i] - lista[i-1] == razaopa):
            return "PA"
        elif (lista[i] / lista[i-1] == razaopg):
            return "PG"
        else:
            return "AG"