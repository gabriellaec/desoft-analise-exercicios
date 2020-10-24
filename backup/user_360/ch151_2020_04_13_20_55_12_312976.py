def classifica_lista(lista):
    cont = 0
    while cont<len(lista)-1:
        if lista[cont+1]>=lista[cont]:
            return 'crescente' 
        elif lista[cont+1]<=lista[cont]:
            return 'decrescente'
        elif len(lista)<2:
            return 'nenhum'
        else:
            return 'nenhum'
    cont+=1