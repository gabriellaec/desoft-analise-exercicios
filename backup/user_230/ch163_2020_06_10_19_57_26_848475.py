def calcula_media(lista):
    notas=0
    alunos=0
    for i in lista:
        for k in i:
            notas+=i[k]
            alunos+=1
    return notas/alunos