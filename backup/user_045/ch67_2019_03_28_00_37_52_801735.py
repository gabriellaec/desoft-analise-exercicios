def alunos_impares(n):
    i=0
    a=[]
    while i<len(n):
        if len(n[i])%2!=0:
            a.append(n[i])
        i+=1
    return a
                
                
    
    