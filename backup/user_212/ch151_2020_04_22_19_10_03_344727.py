
            
def classifica_lista(lista):
    
    if len(lista)<2:
        return 'nunhum'
    
    crescente=True 
    decrescente=False
    i=1
    while i<len(lista):
        if lista[i-1]>=lista[i]: #mesmo que esse seja verdade ele quer verificar o outro 
            crescente=False 
        if lista[i-1]<=lista[i]:
            decrescente=False
        i+=1
    if crescente:
        return 'crescente'
    elif decrescente:
        return 'decrescnte'
    else:
        return 'nenhum'