def verifica_progressao(lista):
    if len(lista) == 0: 
        return 'NA'
    diferença = lista[1] - lista[0]
    divisao = lista[1]/lista[0]
    for i in range(len(lista)):
        if lista[i] - lista[i-1] == diferença:
            return 'PA'
        elif lista[i]/lista[i-1] == divisao:
            return 'PG'
        elif (lista[i] - lista[i-1] == diferença) and (lista[i]/lista[i-1] == divisao):
            return 'AG'
        else:
            return 'NA'
        
    
