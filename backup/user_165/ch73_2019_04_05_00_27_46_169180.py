def remova_vogaiss(x):
    i = 0
    while i < len(x):
        if x[i]=='a' or 'e' or 'i' or 'o' or 'u':
            del x[i]
            return x
        i+=1
    return x  
            