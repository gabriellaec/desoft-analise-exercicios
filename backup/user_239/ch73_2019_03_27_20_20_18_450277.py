def remove_vogais(x):
    i=0
    while i<len(x):
        if x[i]=='a' or x[i]=='e' x[i]=='i' or x[i]=='o' x[i]=='u':
            del x[i]
        i+=1
    return x