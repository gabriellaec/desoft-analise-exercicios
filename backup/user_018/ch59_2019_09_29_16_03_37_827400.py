def conta_a(texto):
    contador = 0
    i = 0
    while i < len(texto):
        if texto[i] == 'a':
        	contador += 1
       		i += 1
        return contador
