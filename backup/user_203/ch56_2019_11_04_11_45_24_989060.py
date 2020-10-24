def calcula_total_da_nota(lista1,lista2):
	nota=0
	i = 0
	while i < len(lista1): 
		nota += lista1[i]*lista2[i]
		i = i +1 
	return nota 


    
    