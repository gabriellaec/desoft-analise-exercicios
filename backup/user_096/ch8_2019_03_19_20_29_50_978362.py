def verifica_progressao(lista):
    i=0
    r=lista[i+1]-lista[i]
    q=lista[i+1]-lista[i]
    while i<len(lista):
        if lista[i+1]+r==lista[i+2]:
            i+=1
            return"PA"
        elif lista[i+1]*q==lista[i+2]:
            i+=1
            return"PG"
        elif lista[i+1]+r==lista[i+2] and lista[i+1]*q==lista[i+2]:
            i+=1
            return"AG"
        else:
            return"NA"
