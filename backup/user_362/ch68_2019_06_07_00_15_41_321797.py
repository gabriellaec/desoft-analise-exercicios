def separa_trios(aluno):
    lista=[]
    qtd = (len(alunos)/3)
    i=0
    while i < int(qtd):
        lista.append(alunos[3*i:3*(i+1)])
        i +=1
        if qtd != int(qtd):
        	lista.append(x[i*3 :])
	return lista