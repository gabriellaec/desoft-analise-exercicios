def remove_vogais(x):
    i = 0
    a = ""
    while i < len(x): 
        if x[i] =! 'a' or x[i] =! 'e' or x[i] =! 'i' or x[i] =! 'o' or x[i] =! 'u':
            a += x[i]
        i+=1    
    return a