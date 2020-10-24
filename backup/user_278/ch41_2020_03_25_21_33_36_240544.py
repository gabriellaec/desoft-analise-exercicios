def zera_negativos(lista):
    a = len(lista)
    contador=0
    
    while contador < a:
        if lista[contador] < 0:
            lista[contador] = 0 
            
            
        	contador= contador + 1
	return (lista)