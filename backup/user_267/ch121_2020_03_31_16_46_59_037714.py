def subtracao_de_listas(a,b):
    lista=[]
	for i in a:
        if i not in b:
            lista.append(i)
    return lista
   
 