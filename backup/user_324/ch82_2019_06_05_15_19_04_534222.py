def primeiras_ocorrencias(pal):
    dic={}
    palavra=[]
    listaocorrencia=[]
    for i in range(len(pal)):
        if i not in palavra:
        	palavra.append(pal[i])
       		listaocorrencia.append(i)
            
            
    for i in range(len(palavra)):
    	dic[palavra[i]]=listaocorrencia[i]
    return dic

        