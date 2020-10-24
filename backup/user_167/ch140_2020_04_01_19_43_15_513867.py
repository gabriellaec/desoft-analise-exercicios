def faixa_notas (l):
    s1=0
    s2=0
    s3=0
    nl=[]
    i=0
    while i < len(l):
        i+=1
        if l[i] < 5:
            s1+=1
        if 5<l[i]<=7:
            s2+=1
        if l[i] > 7:
            s3+=1
        nl.append(s1)
        nl.append(s2)
        nl.append(s3)
    
    return nl
    
        
        