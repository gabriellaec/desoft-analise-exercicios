def alunos_impares(l):
    l_impar=[]
    
    i=0
    
    while i<len(l):
        if i%2!=0 and i!= 0:
            l_impar.append(l[i])
        i+=1