def separa_trios(alunos):
    lista = []
    i = 0
    while i<len(alunos):
        lista.append(lista[i:i+3])  #fatiamento
        i+=3
    return lista