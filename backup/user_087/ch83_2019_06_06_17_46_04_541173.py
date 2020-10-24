def medias_por_inicial(alunos_notas):
    letra_nota = dict()
    for aluno, nota in alunos_notas.items():
        letra_nota[aluno[0]] = nota 
        for m, n in alunos_notas.items():
            if aluno[0] == m[0] and aluno != m:
                letra_nota[aluno[0]] += (n - v)/2
	return letra_nota
        
        