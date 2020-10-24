def remove_vogais(x):
    i=0
    s=''
    while i<len(x):
        if x[i]!='a' or x[i]!='e' or x[i]!='i' or x[i]!='o' or x[i]!='u':
            s+=x[i]
        i+=1
    return s