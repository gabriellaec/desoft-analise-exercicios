def verifica_primos(lista):
    dic = {}
    for primo in lista:
        for i in range(2, primo+1):
	        if i != primo:
		        i = primo % i
		        if i == 0:
			        dic[primo] = False
	        else:
		        dic[primo] = True
		
    return dic