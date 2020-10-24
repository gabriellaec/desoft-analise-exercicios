def quantos_uns(n):
    s = 0
    i = 0
    lista = [int(x) for x in str(n)]
    while i < len(lista):
    	if lista[i] == 1:
        	s += 1
        i += 1
    print(s)
         
