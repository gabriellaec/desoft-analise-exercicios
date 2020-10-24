i = 0
def eh_crescente(lista):
    lista = []
    while i < len(lista):
        if lista[i] < lista[i + 1]:
            i += 1
        return True
        elif lista [i] > lista[i + 1]:
            return False
            
    
    