def verifica_progressao(lista):
    for n in range(len(lista)):
        c=lista[n+1]-lista[n]
        if lista[n+2]-lista[n+1]==c:
                 return("PA")
        cg=lista[n+1]/lista[n]
        if lista[n+2]/lista[n+1]==cg:
            return("PG")
        else:
            return("NA")