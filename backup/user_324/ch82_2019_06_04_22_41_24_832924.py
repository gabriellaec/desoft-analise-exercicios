def primeiras_ocorrencias(pal,valor):
    dic={}
    palavra=[]
    listaocorrencia=[]
    for i in range(len(pal)):
        if i not in palavra:
        	palavra.append(i)
	for i in range(len(palavra)):
        dic[palavra[i]]=listaocorrencia[i]
    return dic

        