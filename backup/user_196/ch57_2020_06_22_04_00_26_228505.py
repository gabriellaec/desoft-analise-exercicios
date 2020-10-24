def verifica_progressao(lista):
    razaopa = lista[1] - lista[0]
    razaopg = lista[1]*lista[0]
    for i in range(len(lista)-1):
        if (lista[i] - lista[i-1] == razaopa):
            return "PA"
        elif (lista[i] / lista[i-1] == razaopg):
            return "PG"
        else:
            return "AG"