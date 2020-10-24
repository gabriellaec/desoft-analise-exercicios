def classifica_lista(lista):
    i = 0
    cresc = True
    decresc = True
    if lista[1] > lista[0]:
        while i <= len(lista):
            if lista[i+1] <= lista[i]:
                cresc = False
                break
            else:
                i += 1
                cresc == True
                decresc = False
    elif lista[1] < lista[0]:
        while i <= len(lista):
            if lista[i+1] >= lista[i]:
                decresc = False
                break
            else:
                i += 1
                decresc == True
                cresc = False
        
    else:
        return 'nenhum'

    if cresc == True:
        return 'crescente'
    elif decresc == True:
        return 'decrescente'
    else:
        return 'nenhum'
            