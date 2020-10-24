def verifica_progressao(lista):
    x="nada"
    i=1
    while i<len(lista)-1:
        if lista[i]/lista[i-1]==lista[i+1]/lista[i]:
            x="PG"
            i=i+1
        elif lista[i]-lista[i-1]==lista[i+1]-lista[i]:
            x="PA"
            i=i+1
        else:
            x="NA"
            i=i+1
    return x
