def verifica_numero(x):
    y = [x] 
    n = len(y)-1
    i = 0
    soma = 0
    
    while y[i] < n:
        soma = soma + y[i]**y[i]
        if soma == y:
            return True
        else:
            return False
        i+=1        
        