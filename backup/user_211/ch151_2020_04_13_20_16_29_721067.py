def estritamente_decrescente(lista):
    eh_ou_nao_eh= all(x > y for x, y in zip(lista, lista[1:])) 
    return eh_ou_nao_eh
def estritamente_crescente(lista):   
    eh_ou_nao_eh = all(x > y for x, y in zip(lista, lista[1:])) 
    return eh_ou_nao_eh
def classifica_lista(lista):
    if estritamente_decrescente(lista)==True and not len(lista)<=1:
        return 'decrescente'
    elif estritamente_crescente(lista)==True and not len(lista1)<=1:
        return 'crescente'
    else:
        return'nenhum'

    
    