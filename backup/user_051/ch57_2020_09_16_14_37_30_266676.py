def verifica_progressao(lista_ag):
    razao_pa=lista_ag[1]-lista_ag[0]
    pa=True
    razao_pg=lista_ag[1]/lista_ag[0]
    pg=True
    i=0
    while i<len(lista_ag)-1:
        if lista_ag[i+1]!=lista_ag[i]+razao_pa:
            pa=False
        if lista_ag[i+1]!=lista_ag[i]*razao_pg:
            pg=False
        i+=1
    if pa and pg:
        return 'AG'
    if pg:
        return 'PG'
    if pa:
        return 'PA'
    else:
        return 'NA'