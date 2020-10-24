def interseccao_chaves(d1,d2):
    ls1=[]
    ls2=[]
    ls3=[]
    for n in d1:
        ls1.append(n)
    for i in d2:
        ls2.append(i)
    for i in ls1:
        for n in ls2:
            if i==n:
                ls3.append(i)
    
                
    
    return ls3
        