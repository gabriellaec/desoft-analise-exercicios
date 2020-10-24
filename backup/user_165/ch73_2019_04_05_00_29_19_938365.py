def remove_vogais(x):
    i = 0
    while i < len(x):
        if x[i]=='a' or 'e' or 'i' or 'o' or 'u':
            del x[i]
        i+=1
    return x  
            