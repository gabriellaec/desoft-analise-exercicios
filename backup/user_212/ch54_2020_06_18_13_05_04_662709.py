def calcula_fibonacci(n):
    F = []
    c1 = 1
    c2 = 1
    if n == 0 :
        F=[]
    elif n == 1 :
        F.append(c1)
    elif n == 2: 
        F.append(c1)
        F.append(c2)
    else:
        F.append(c1)
        F.append(c2)
        i = 3 
        while i <= (n-2):
            m = (i-1) + (i-2)
            F.append(m)
            i += 1
    return F