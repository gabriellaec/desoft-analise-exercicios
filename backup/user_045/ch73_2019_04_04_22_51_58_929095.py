def remove_vogais(n):#deu certo no spyder
    
    i=0
    v=[]
    while i<len(n):
        if n[i]!='a' and n[i]!='i' and n[i]!='e' and n[i]!='u' and n[i]!='o':
            v.append(n[i])
        i+=1
   
    return str(v)