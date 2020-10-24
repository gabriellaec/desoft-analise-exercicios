def remove_vogais(palavra):
    i=0
    x=palavra.lower()
    palavra2=[]
    while i<len(x):
        if x[i]!='a' and x[i]!='e' and x[i]!='i' and x[i]!='o' and x[i]!='u':
            palavra2.append(x[i])
        i+=1
    return ''.join(palavra2)