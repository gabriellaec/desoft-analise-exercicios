def verifica_progressao(lista):
    i = 0
    while i < len(lista):
        if lista[i+1] - lista[i] == lista[i+2] - lista[i+1]:
            return "PA"
        if lista[i+1] == lista[i]*(lista[i+1]-lista[i]):
            return "PG"
        else:
            return "NA" 