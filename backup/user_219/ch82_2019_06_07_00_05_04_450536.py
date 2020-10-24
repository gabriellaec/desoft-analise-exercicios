def primeiras_ocorrencias(string):
    dic={}
    caracteres=[]
    index=[]
    for i in range(len(string)):
        if string[i] not in caracteres:
            caracteres.append(string[i]
            index.append(i)
     for indice in range(len(caracteres)):
         dic[caracteres[indice]]= index[indice]
     return dic