def verifica_progressao(lista):
    pa=1
    pg=1
    count=0
    tamanho_lista=len(lista)-1
    razao_pa=lista[1]-lista[0]
    razao_pg=lista[1]/lista[0]
    while count < tamanho_lista and pg==1:
        if lista[count] == 0:
            pg=0
        count+=1
    count=0
    if pa==1:
        while count < tamanho_lista and pa==1:
            if lista[count+1]-lista[count] != razao_pa:
                pa=0
            count +=1
    count=0
    if pg==1:
        while count < tamanho_lista and pg==1:
            if lista[count+1]/lista[count] != razao_pg:
                pg=0
            count +=1
    if len(lista) == 2:
        pa=1
    if pg==1 and pa==1:
        return 'AG'
    elif pg==1:
        return 'PG'
    elif pa==1:
        return 'PA'
    elif pa==0 and pg==0:
        return 'NA'