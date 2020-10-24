def calcula_total_da_nota(lista1,lista2):
    nota=0
    i = 0
    listanota = []
    while i < len(listanota): 
        listanota[i] = lista1[i]*lista2[i]
        nota = nota + listanota[i]
        i = i +1 
	return nota 


    
    