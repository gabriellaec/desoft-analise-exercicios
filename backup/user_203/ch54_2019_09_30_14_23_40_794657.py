def junta_nome_sobrenome (lista1,lista2):
	lista = []
	i = 0 
	nomecompleto = "" 
	while i < len(lista1):
		nomecompleto =  lista1[i]+" "+lista2[i]
		lista.append(nomecompleto)
		i+=1 
	return lista 
    
        
        