def verifica_progressao(lista):
    if lista[0]==0:
        cont = 0
        for i in lista:
            if i!=0:
               	cont+=1
        if cont==0:
            return 'AG'
		else:
            cont = 0
            r = lista[1]-lista[0]
            for i in range(len(lista)-1):
                if lista[i+1]-lista[i] == r:
                    cont += 1
                if cont == len(lista)-1:
                    return 'PA'
                else:
                    return 'NA'
	else:
        cont_a = 0
        cont_g = 0
        r = lista[1]-lista[0]
        q = lista[1]/lista[0]
        for i in range(len(lista)-1):
            if lista[i+1]-lista[i]==r:
                cont_a += 1
           	if lista[i+1]/lista[i] == q:
                cont_g += 1
        if cont_a == len(lista)-1:
            if cont_g == len(lista)-1:
                return 'AG'
            else:
                return 'PA'
        if cont_g == len(lista)-1:
            return 'PG'
return 'NA'