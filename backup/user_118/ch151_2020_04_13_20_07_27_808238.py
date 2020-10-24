def classifica_lista(lista):
    i=0
    while i<len(lista)>2:
        if valores[i]>valores[i+1]:
            return 'decrescente' 
        elif valores[i+1]>valores[i]:
            return 'crescente'
        else:
            return 'nenhum'
    while len(lista)<2:
        return 'nenhum'
