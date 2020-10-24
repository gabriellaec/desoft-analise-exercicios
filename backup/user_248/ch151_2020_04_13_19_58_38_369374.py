def classifica_lista(lista):
    l=sorted(lista)
    if len(lista)<2:
        return 'nenhum'
    elif lista==l:
        return 'crescente'
    elif lista==l[::-2]:
        return 'decrescente'
    else:
        return 'nenhum'
        
    
    