def remove_vogais (x):
    y=''
    i=0
    while i < len(x):
        if x[i] not in ['a','e','i','o','u']:
            y+=x[i]
        i+=1
    return y
        
    
    

    