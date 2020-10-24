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
    for numeros in lista:
        if eh_crescente(numeros):
            return 'crescente'
        if eh_descrescente(numeros):
            return 'descrescente'
        if lista == []:
            return 'nenhum'
        if len(lista) < 2:
            return 'nenhum'
        else:
            return 'nenhum'
        
        
        
        
            
            