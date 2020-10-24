def verifica_progressao(lista):
    razao_pa = lista[i+1]-lista[i]
    razao_pg = lista[i+1]/lista[i]

    for i in range(len(lista)):
        if razao_pa == lista[i+3]-lista[i+2] and razao_pg == lista[i+3]/lista[i+2]:
            print('AG')
        elif razao_pa == lista[i+3]-lista[i+2]:
            print('PA')
        elif razao_pg == lista[i+3]/lista[i+2]:
            print('PG')
        else:
            print('NA')