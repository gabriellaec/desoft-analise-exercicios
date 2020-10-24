def estritamente_crescente(num):
    lista = [1,3,2,5,8,6,9]
    listaCresc = []
    listaCresc.append(lista[0])
    
    i = 1
    valorArmazenado = lista[0]
    for i in range lista:
        if i > valorArmazenado:
            valorArmazenado = lista[i]
    		listaCresc.append(lista[i])
	
    return estritamente_crescente

    