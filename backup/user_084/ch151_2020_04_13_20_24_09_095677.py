def classifica_lista(l):
    if len(l)==0 or len(l)==1:
        print('nenhum')
    elif len(l)>=2:
        if l[0]>l[1]:
            return('decrescente')
        elif l[0]<l[1]:
            return('crescente')
        else:
            return('nenhum')
   
    
    