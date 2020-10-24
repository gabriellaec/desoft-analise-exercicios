def acha_bigramas(palavra):
    cont=1
    lista_vazia=[]
    while cont<len(palavra) and cont>=1:
        if palavra[cont] == palavra[cont-1]:
        	lista_vazia.append(palavra[cont])
    	cont+=1
    return lista_vazia
        