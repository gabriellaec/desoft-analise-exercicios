def acha_bigramas(palavra):
    cont=0
    lista_vazia=[]
    while cont<len(palavra):
        if palavra[cont] == palavra[cont-1] and cont>=0:
        	lista_vazia.append(palavra[cont])
    	cont+=1
    return lista_vazia
        