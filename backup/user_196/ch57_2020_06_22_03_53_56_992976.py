def verifica_progressao(lista):
    k = 2
    for i in range(len(lista)):
        if lista[i] == lista[i-1] + k:
            return "PA"
        elif lista[i] == lista[i-1] * k:
            return "PG"
        else:
            return "AG"