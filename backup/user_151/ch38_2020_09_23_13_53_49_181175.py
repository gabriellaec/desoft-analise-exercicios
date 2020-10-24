def quantos_uns(n):
    y = str(n)
    i=0
    x=0
    while i<len(y):
        if y[i] == '1':
            x = x + 1
        i = i + 1
    return x
      
            
        
    