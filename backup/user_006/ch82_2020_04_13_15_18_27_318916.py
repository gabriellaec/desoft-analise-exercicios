def primeiras_ocorrencias(palavra):
    dicio={}
    lista=[]
    for i in palavra:
        if i not in lista:
            lista.append(palavra.index(i))     
            dicio[i]=palavra.index(i)
    return dicio
       
                
                