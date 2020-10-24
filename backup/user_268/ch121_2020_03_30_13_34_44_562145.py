def subtracao_de_listas(L1, L2):
    a=len(L1)
    b=len(L2)
    q=0
    w=0
    L3=[]
    if a == 0:
        return L2
    if b==0:
        return L1
    while w != (b-1):
        while q<a:
        if L1[q] != L2[w]:
            q+=1
            if q == a-1:
                L3.append[q]
                w+=1
                q=0
    
    return L3
            
            
            
   