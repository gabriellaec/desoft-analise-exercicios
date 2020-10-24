def forma_trios(lista_alunos):
    cont=0
    lista_trios=[]
    while cont<len(lista_alunos):
        lista_trios.append(lista_alunos[cont:cont+3])
        cont+=3
    return lista_trios