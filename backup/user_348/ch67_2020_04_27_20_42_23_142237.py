def alunos_impares (nomes):
    impares = []
    alunos = nomes[1::2]
    impares.append(alunos)
    return impares

print(alunos_impares (['Aluno 0']))
       