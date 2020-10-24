def calcula_media(lista):
    n_alunos = 0
    notas = 0
    for dic in lista:
        for nota in dic.values():
            notas += nota
            n_alunos += 1
    return notas/n_alunos
   
             
        