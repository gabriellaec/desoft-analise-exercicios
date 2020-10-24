def eh_crescente (lista):
    if(len(lista) > 1):
        i = 1
        var = True
        while i < len(lista):
            if(lista[i] < lista[i-1]):
                var = False
            else:
                var = True
            i += 1
        return var