def eh_crescente(x):
    a = 1
    while a<len(x):
        if x[a-1] < x[a]:
            a+=1
        else:
            return False
    return True

def eh_decrescente(x):
    a = 1
    while a<len(x):
        if x[a-1] > x[a]:
            a+=1
        else:
            return False
    return True


def classifica_lista(lista):
    if lista == []:
        return 'nenhum'
    if len(lista) < 2:
        return 'nenhum'
    if eh_crescente(lista):
        return 'crescente'
    if eh_decrescente(lista):
        return 'decrescente'
    else:
        return 'nenhum'
        
        
        
        
            
            