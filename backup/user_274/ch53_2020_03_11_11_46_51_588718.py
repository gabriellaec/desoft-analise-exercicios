def soma_impares(list):
    n = len(list)
    i = 0
    s = 0
    
    while i < n:
        if list[i] % 2 > 0:
            s=s+list[i]
        i=i+1
    return s