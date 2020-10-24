
def junta_nome_sobrenome (l1,l2):
    
    lista=[]
    i=0
    
    while(i<len(l1)):
    
        r= l1[i]+ " " + l2[i]
        lista.append(r)
        i+=1
    
    return lista