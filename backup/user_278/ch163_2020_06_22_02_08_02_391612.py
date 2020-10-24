def calcula_media(lista):
    #i pega cada dicionário respectivo a cada sala
    alunos = 0
    notas = 0
    for i in lista:
        #to dentro do dicionário
        for aluno, nota in i.items():
            notas += nota
            alunos +=1
    return notas/alunos