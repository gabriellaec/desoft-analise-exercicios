def classifica_lista(lista):
    i=0
    diferenca=lista[i+1]-lista[i]
    if len(lista)<2:
        return 'nenhum'
    while i<len(lista):
        if diferenca>0:
            while diferenca>0:
            i+=1
            return 'crescente'
        elif diferenca<0:
            while diferenca <0:
            i+=1
            return 'decrescente'
        else:
            return 'nenhum'