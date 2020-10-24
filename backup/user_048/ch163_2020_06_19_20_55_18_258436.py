def calcula_media(lista):
    notas=0
    alunos=0
    for dicio in lista:
        for value in dicio.values():
            notas+=value
            alunos+=1
    return notas/alunos