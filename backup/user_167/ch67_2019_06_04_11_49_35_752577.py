def alunos_imparesn(x):
    i=0
    d=[]
    while i < len (x):
        if i % 2!=0:
            d.append (x[i])
        i+=1
    return d
            
            