def eh_crescente (lista):
    if(len(lista) > 1):
        i = 1
        var = True
        while i < len(lista) and var:
            if(lista[i] < lista[i-1]):
                var = False
            i += 1
                
        return var