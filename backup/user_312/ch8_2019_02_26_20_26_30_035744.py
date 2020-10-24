def verifica_progressao(lista):
    pa=1
    pg=1
    tamanho_lista=len(lista)-1
    if lista[1]-lista[0] == lista[2]-lista[1]:
        razao_pa=lista[1]-lista[0]
    else:
        pa=0
    if lista[1]/lista[0] == lista[2]/lista[1]:
        razao_pg=lista[1]/lista[0]
    else:
        pg=0
    if pa==1:
        while count < tamanho_lista and pa==1:
            if lista[count+1]-lista[count] != pa:
                pa=0
            count +=1
        count=0
    if pg==1:
        while count < tamanho_lista and pg==1:
            if lista[count+1]/lista[count] != pg:
                pg=0
            count +=1
    if pg==1 and pa==1:
        return 'AG'
    elif pg==1:
        return 'PG'
    elif pa==0:
        return 'PA'
    else:
        return 'NA'