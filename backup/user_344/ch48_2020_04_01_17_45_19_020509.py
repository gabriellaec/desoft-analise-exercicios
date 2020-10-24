def eh_crescente(lista):
    i=0
    listav = []
    if len(lista) == 0:
        return listav
    elif len(lista) ==1:
        return lista
    else:
        while i< len(lista):
            if lista[i]> lista[i-1]:
                return True
            else:
                return False
            i+=1
        
        
