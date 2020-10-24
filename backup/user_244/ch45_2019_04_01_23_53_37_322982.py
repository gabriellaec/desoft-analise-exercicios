def zera_negativos(x):
    i = 0
    
    z = []
    
    
    while i < len(x):
        if x[i] < 0:
            z.append(0)
        else:
            z.append(x[i])
        
        i += 1
    return z 

x = [1,-1,2,-2,3,-3]

print(zera_negativos(x))