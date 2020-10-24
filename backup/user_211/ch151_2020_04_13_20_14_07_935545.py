def estritamente_decrescente(lista):
    eh_ou_nao_eh= all(x > y for x, y in zip(lista, lista[1:])) 
    return eh_ou_nao_eh
def estritamente_crescente(lista):   
    eh_ou_nao_eh = all(x > y for x, y in zip(lista, lista[1:])) 
    return eh_ou_nao_eh
def classifica_lista(lista):
    if len(lista)<=1:
        return 'nenhum'
    elif estritamente_decrescente(lista)==True:
        return 'decrescente'
    elif estritamente_crescente(lista)==True:
        return 'crescente'

    
    