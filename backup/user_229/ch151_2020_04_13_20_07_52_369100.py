def classifica_lista(lista):
    cresc = True
    decresc = True
    if len(lista) <= 1:
        return 'nenhum'
    else:
        if lista[1] > lista[0]:
            decresc = False
            for i in range(1,len(lista)):
                if lista[i] <= lista[i-1]:
                    cresc = False
                    break
                else:
                    i += 1
                    cresc == True
                    
        elif lista[1] < lista[0]:
            cresc = False
            for i in range(1,len(lista)):
                if lista[i] >= lista[i-1]:
                    decresc = False
                    break
                else:
                    i += 1
                    decresc == True
            
        else:
            return 'nenhum'

    if cresc == True:
        return 'crescente'
    elif decresc == True:
        return 'decrescente'
    else:
        return 'nenhum'