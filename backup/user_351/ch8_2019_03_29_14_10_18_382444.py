def verifica_progressao(numeros):
    i = 0
    c = 0
    while i<len(numeros)-2:
        if numeros[i + 1] - numeros[i] != numeros[i + 2] - numeros[i+1]:
            c+=1
        i+=1
        
    d = 0
    while i<len(numeros)-2:
        if numeros[i + 1]/numeros[i] != numeros[i + 2] / numeros[i+1]:
            d+=1
        i+=1
    if c = 0 :
        return "PA"
    elif d = 0:
        return "PG"
    elif c = 0 and d = 0:
        return "AG"
    else:
        return "NA"
    