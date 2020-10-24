def remove_vogais (x):
    y=''
    i=0
    while i < len(x):
        i+=1
        if x[i] not in ['a','e','i','o','u']:
            y+=x[i]
        
    return y
        
    
    

    