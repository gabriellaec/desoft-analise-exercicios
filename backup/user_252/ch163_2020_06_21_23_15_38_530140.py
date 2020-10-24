def calcula_media(escola):
    alunos=0
    notas=0
    for turma in escola:
        for nota in turma.values():
            notas+=nota
            alunos+=1
    return (notas/alunos)
            
    