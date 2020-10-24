def verifica_primos(lista):
    dic_primos = {}
    for e in lista:
        if primos(e) == True:
        	dic_primos[e] = True
        else:
            dic_primos[e] = False
	return dic_primos

def primos(x):
    Div =2
    
    while Div < x :
        
        if x % Div == 0:
            return False
        else:
            Div += 1
    return True