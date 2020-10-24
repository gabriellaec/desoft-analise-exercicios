def quantos_uns (x):
    y=str(x)
    i=0
    s=0
    while y[i] < len (y):
        i+=1
        if y[i]== 1:
            s+=1
    return s  
            
    