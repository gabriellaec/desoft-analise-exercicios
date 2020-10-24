def acha_bigramas(palavra):
    palavra=list(palavra)
    lista=[]
    i=0
    while(i<len(palavra)-1):
        if(palavras[i]+palavra[i+1] not in lista):
            lista.append(palavra[i]+palavra[i+1])
        i=+1
    return lista
       