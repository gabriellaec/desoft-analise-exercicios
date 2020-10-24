def classifica_lista(l):
    if len(l)<2:
        return "nenhum"
    i=l[1]-l[0]
  
    if i>0:
        for i in range (len(l)-1):
            if l[i+1]-l[i]<=0:
                return "nenhum"
    if i<0:
         for i in range (len(l)-1):
            if l[i+1]-l[i]>=0:
                return "nenhum"
            
    if l==0:
        return "nenhum"
    elif l>0:
        return "crescente"
    elif l<0:
        return "decrescente"
    