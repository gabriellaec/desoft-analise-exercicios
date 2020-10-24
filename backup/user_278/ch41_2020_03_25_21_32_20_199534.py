def zera_negativos(lista):
    contador=0
    a = len(lista)
    while contador < a:
        if lista[contador]<0:
            lista[contador] = 0 
        contador= contador + 1
	return (lista)