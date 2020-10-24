def calcula_fibonacci (n):
    
    F = [0]*n
    
    if n == 0:
        F = []
    elif n == 1:
        F[0] = 1
    elif n == 2:
        F[0] = 1
        F[1] = 1
      
    else: 
        F[0] = 1
        F[1] = 1
        for i in range (0, (len(F)-2)):
            F[i] = F[i-1] + F[i-2]
            
    return F