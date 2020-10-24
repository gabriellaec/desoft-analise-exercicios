def verifica_lista(lista):
    verif=[]
    for i in lista:
        if i % 2 == 0:
            verif.append(i)
    if lista==[]:
        return 'misturado'
    elif len(verif) == len(lista):
        return 'par'
    elif verif == []:
        return 'ímpar'
    else:
        return 'misturado'