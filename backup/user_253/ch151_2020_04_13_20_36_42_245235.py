def classifica_lista (lista):
    i=0
    while i> len(lista) and len(lista) > 1:
        if lista[0+i] < lista[1+i]:
            i=i+1
        return 'crescente'
        if lista[1+i]< lista[0+i]:
            i+=1
        return 'decrescente'
        if lista[1+i]< lista[0+i]==false and lista[0+i] < lista[1+i]==false:
            return 'nenhum'
    if len(lista) < 1:
        return 'nenhum'
    
  
   
    
    
    