def verifica_progressao(lista):
    for e in len(lista):
        if lista[e+1] - lista[e] == lista[e]-lista[e-1]:
            return "PA"
        if lista[e+1]/lista[e] == lista[e]-lista[e-1]:
            return "PG"
        elif [e+1] - lista[e] == lista[e]-lista[e-1] and lista[e+1]/lista[e] == lista[e]-lista[e-1]:
            return "AG"
        else:
            return "NA"