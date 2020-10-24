def classifica_lista (lista):
    crescente = 'crescente'
    decrescente = 'decrescente'
    nenhum = 'nenhum'
    
    if len(lista) >= 2:
        i = 0
        #Estritamente Crescente
        if lista[i+1] > lista[i]:
            maior = lista[i+1]
            while i < len(lista):
                if lista[i+1] > maior:
                    maior = lista[i+1]
                    i = i + 1
                else:
                    return nenhum
            return crescente
        #Estritamente Decrescente
        elif lista[i+1] < lista[i]:
            menor = lista[i+1]
            while i < len(lista):
                if lista[i+1] < menor:
                    menor = lista[i+1]
                    i = i + 1
                else:
                    return nenhum
            return decrescente
        #Nenhum dos dois
        else:
            return nenhum
    else:
        return nenhum