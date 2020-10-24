def remove_vogais(x):
    i = 0
    a = ""
    while i < len(x): 
        if x[i] != 'a' and x[i] != 'e' and x[i] != 'i' and x[i] != 'o' and x[i] != 'u':
            a += x[i]
        i+=1    
    return a