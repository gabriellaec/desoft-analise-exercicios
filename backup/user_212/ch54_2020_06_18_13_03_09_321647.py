def calcula_fibonacci(n):
    F = []
    
    if n == 0 :
        F=[]
    if n == 1 :
        F.append(1)
    if n == 2: 
        F.append(1)
        F.append(2)
    else:
        F.append(1)
        F.append(2)
        while i < (n-2):
            m = (i-1) + (i-2)
            F.append(m)
    return F