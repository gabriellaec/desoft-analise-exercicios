def classifica_lista(lista):
    i = 0
    contador_crescente = 0
    contador_decrescente = 0
    if len(lista)> 1:
        for i in lista -1:
            if lista[i+1] > lista[i]:
                contador_crescente += 1
            i += 1
            if contador_crescente == len(lista):
                return "crescente"
            elif lista [i+1] < lista[i]:
                contador_decrescente += 1
            i += 1
            if contador_decrescente == len(lista):
                return "decrescente"
            else:
                return "nenhum"
    else lista[0] > lista[1]:
            return "crescente"
        elif lista[0] < lista[1]:
            return "decrescente"
        else:
            return "nenhum"
                    
            
                