def alunos_impares(lista):
    liste=[]
    for e in lista:
        if lista.index(e)%2!=0:
            liste.append(e)
    return liste