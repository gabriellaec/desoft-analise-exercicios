def alunos_impares (alunos):
    listanova=[]
    for i,aluno in enumerate (alunos):
        if i%2!=0:
            listanova.append (aluno)
    return listanova