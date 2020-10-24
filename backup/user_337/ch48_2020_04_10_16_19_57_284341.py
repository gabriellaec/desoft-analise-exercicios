def estritamente_crescente(lista):
    lista_cresce = []
    if len(lista)>0:
        lista_cresce = [lista[0]]
    else: return lista_cresce
    i = 1
    a = 0
    while i < len (lista):
        if lista[i] > lista_cresce[a]:
            lista_cresce.append(lista[i])
            a += 1
        i += 1
    return lista_cresce
            
def eh_crescente (lista):
    if estritamente_crescente(lista) == lista:
        return True
    else:
        return False
    
    
        