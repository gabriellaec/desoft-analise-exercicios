def subtracao_de_listas(lista1, lista2):
    nova_lista = []
    if len(lista2)==0:
        nova_lista = lista1
    else:
        for i in lista1:
            for j in lista2:
                if (i not in lista2):
                    nova_lista.append(i)
                    break
    return(nova_lista)
	
 

                
        