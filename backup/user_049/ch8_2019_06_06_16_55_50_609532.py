def verifica_progressao(lista):
    
    for i in range(len(lista)):
        razao_pa = lista[i+1]-lista[i]
        razao_pg = lista[i+1]/lista[i]
        
        if lista[i] == '0':
        	return('NA')
        if razao_pa == lista[i+3]-lista[i+2] and razao_pg == lista[i+3]/lista[i+2]:
            return('AG')
        elif razao_pa == lista[i+3]-lista[i+2]:
            return('PA')
        elif razao_pg == lista[i+3]/lista[i+2]:
            return('PG')
        else:
            return('NA')
