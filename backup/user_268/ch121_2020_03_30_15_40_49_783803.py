def subtracao_de_listas(L1, L2):
    a=len(L1)
    b=len(L2)
    q=0
    L3=[]
    while q<a:
        c=0
        y=0
        while y<b:
            if L1[q]!=L2[y]:
                y+=1
                c+=1
            else:
                y+=1
        if b==c:
            L3.append(L1[q])
            x+=1
        else:
            x+=1
    return L3
            
   