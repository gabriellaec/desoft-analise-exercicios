def interseccao_chaves(dic1,dic2):
    lista=[]
    lista_final=[]
    for e in dic1.keys():
        lista.append(e)
    for i in dic2.keys():
        lista.append(i)
    for a in lista:
        for a in dic1.keys() and a in dic2.keys():
        	if a not in lista_final:
            	lista_final.append(a)
    return lista_final