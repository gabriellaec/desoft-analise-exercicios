def calcula_media(alunos):
    num_alunos = 0
    total = 0
    for turma in alunos:
        for aluno in turma:
            num_alunos += 1
            total += alunos[turma][aluno]
            
    return total/num_alunos
            