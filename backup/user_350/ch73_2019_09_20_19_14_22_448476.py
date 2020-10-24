def remove_vogais(n):
    a=[]
    i=0
    while i<len(n):
        if n[i]!= 'a'or n[i]!='e'or n[i]!='i'or n[i]!='o'or n[i]!='u':
            a.append(n[i])
            i+=1
        return a
            
            
            
    