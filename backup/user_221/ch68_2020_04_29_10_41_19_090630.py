def separa_trios(alunos):
	lista =[]
	i = 0
	while i < len(alunos):
		trios = alunos[i:i+3]
		lista.append(trios)
		i += 3
	return lista