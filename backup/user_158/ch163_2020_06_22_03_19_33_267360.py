def calcula_media(lista):
    alunos = 0
    notas = 0
    for i in lista:
        for aluno, nota in i.items():
            notas += nota
            alunos +=1
    return notas/alunos