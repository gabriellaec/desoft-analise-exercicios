def remove_vogais(n):
    a=""
    i=0
    while i<len(n):
        if n[i]!= 'a'and n[i]!='e' and n[i]!='i' and n[i]!='o' and n[i]!='u':
            a+= n[i]
        i+=1
    return a
            
            
            
    