def classifica_lista(l):
    l=[]
    if len(l)==1 and len(l)==0:
        print('nenhum')
    elif len(l)>=2:
        if l[0]>l[1]:
            return('decrescente')
        elif l[0]<l[1]:
            return('crescente')
        else:
            return('nenhum')
   
    
    