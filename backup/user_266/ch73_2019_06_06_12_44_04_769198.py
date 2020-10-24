def remove_vogais(palavra):
    i=0
    x=palavra.lower()
    palavra2=[]
    while i<len(x):
        if x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u':
            palavra2.append(x.replace(x[i], ''))
        i+=1
    return palavra2[0]