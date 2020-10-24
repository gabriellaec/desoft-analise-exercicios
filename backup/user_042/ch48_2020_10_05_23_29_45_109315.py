lista = []
def eh_crescente(lista):
    i = 1
    while i < len(lista):
        if lista[i-1] < lista[i]:
            return True
        else: 
            return False
        i += 1