def verifica_progressao(numeros):
    i = 0
    while i<len(numeros):
        if numeros[i + 1] - numeros[i] == numeros[i + 2] - numeros[i+1]:
            return "PA"
        elif numeros[i + 1]/numeros[i] == numeros[i + 2] / numeros[i+1]:
            return "PG"
        elif numeros[i + 1] - numeros[i] == numeros[i + 2] - numeros[i+1] and numeros[i + 1]/numeros[i] == numeros[i + 2] / numeros[i+1]:
            return "AG"
        else:
            return "NA"
    i+=1
        