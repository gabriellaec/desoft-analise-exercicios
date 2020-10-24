def soma_impares(a):
    i = 0
    b = []
    while  i < len(a):
        if a[i] % 2 != 0:
            b.append(a[i])
    j = 0
    y = 0
    while j<len(b):
        y = y + b[j]
        
    return y
        
         
        