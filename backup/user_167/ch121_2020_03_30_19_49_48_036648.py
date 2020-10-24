def subtracao_de_listas(l1,l2):
    nova_l=[]
    i=0
    while l1[i]<len(l2):
        if i  not in l2:
            nova_l.append(i)
            i+=1
        i+=1
    return nova_l
        
    
    