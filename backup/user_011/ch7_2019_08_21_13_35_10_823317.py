def calcula_norma(lista):
    if len(lista) == 3:
        i = 0
        while i < len(lista):
            vetor = (i[0]**2 + i[1]**2 + i[2]**2)**0.5
        i+= 1
     
    return vetor
	
    if len(lista) == 2:
        i = 0
        while i<len(lista):
            vetor = (i[0]**2 + i[1]**2)**0.5
            i+=1
            return vetor
    if len(lista) == 1:
        vetor = lista[0]
        return vetor
        
       