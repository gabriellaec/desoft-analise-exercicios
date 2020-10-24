def classifica_lista(lista):
    i=1
    if len(lista)<2:
        return 'nenhum'
    else:
        while i<len(lista):
            if lista[i]>lista[i-1]:
                pass
                if lista[i]==lista[-1]:
                    return 'crescente'
            elif lista[i]<lista[i-1]:
                pass
                if lista[i]==lista[-1]:
                    return 'decrescente'
            else:
                return 'nenhum'
                break
            i+=1