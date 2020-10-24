def quantos_uns (numero):
    x = list(numero)
    i = 0
    n = 0
    while i < len(x):
        if x[i] == 1:
            n+=1
        i+=1
    return n        
       
        
        