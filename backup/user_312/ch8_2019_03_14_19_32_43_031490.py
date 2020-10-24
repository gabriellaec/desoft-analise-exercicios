def verifica_progressao(lista):
    pa=1
    pg=1
    count=0
    tamanho_lista=len(lista)-1
    razao_pa=lista[1]-lista[0]
    razao_pg=lista[1]/lista[0]
    while count <= tamanho_lista and pa==1: #Verifica PA
        if lista[count+1]-lista[count] != razao_pa:
            pa=0
        count +=1
    count=0
    if pg==1:
    	while count <= tamanho_lista and pg==1: #verifica PG
            if lista[count+1]/lista[count] != razao_pg or lista[count]==0:
                pg=0
            count +=1
    count=0
    if len(lista) <= 2: #toda lista de 2 numeros é uma pa ¯_(ツ)_/¯
        pa=1
        pg=1
    if pg==1 and pa==1:
        return 'AG'
    elif pg==1:
        return 'PG'
    elif pa==1:
        return 'PA'
    else:
        return 'NA'