def arcotangente(x,n):
    i = 1
    s = 1
    j = 5 #sempre que 5, 9, 13 são somados, eles são positivos
    t = 3 #sempre que 3,7,,11 e etc são somados, eles são negativos
    
    while i <= n and n > 1:
        
        if s == 1:
            resu = (x**s)/s
              
        elif s == t:
            resu += -(x**s)/s
            t += 4
        elif s == j:
            resu += (x**s)/s
            j += 4
        
        s += 2
        i +=1
    return (resu)
