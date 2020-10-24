def classifica_lista(lista):
    if len(lista)<2:
        return 'nenhum'
    crescente=False
    decrescente=False
    if lista[1]-lista[0]>0:
        crescente=True
        i=1
        while i<len(lista) and crescente:
            diferenca=lista[i]-lista[i-1]
            if diferenca<=0:
                crescente=False  
            i+=1
    
    elif lista[1]-lista[0]<0:
        decrescente=True
        i=0
        while i<len(lista) and decrescente:
            diferenca=lista[i]-lista[i-1]
            if diferenca>=0:
                decrescente=False     
            i+=1
    
    if crescente:
        return "crescente"
    elif decrescente:
        return "decrescente"
    else:
        return "nenhum"