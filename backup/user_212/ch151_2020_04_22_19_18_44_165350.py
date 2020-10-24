
            
def classifica_lista (lista):
    
    if len(lista)<2:
        return 'nenhum' 
    
    crescente=True 
    decrescente=True 
    
    i=1
    while i< len(lista):
        if lista[i-1]<=lista[i]:
            crescente=False 
        if lista[i-1]>=lista[i]:
            decrescente=False
        i+=1
        
    if crescente == True:
        return 'crescente'
    elif decrescente == True:
        return 'decrescente'
    else:
        return 'nenhum'