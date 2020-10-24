def numero_no_indice(listaIn):
    i=0
    numIndice=[]
    while i<len(listaIn):
        if listaIn[i]==i:
            numIndice.append(i)
        i+=1
    return(numIndice)

        
        