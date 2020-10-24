def remove_vogais(x):
    i=0
    s=''
    while i<len(x):
        if x[i]!='a' and x[i]!='e' and x[i]!='i' and x[i]!='o' and x[i]!='u':
            s+=x[i]
        i+=1
    return s