def classifica_lista(l):
    l=[]
    if len(l)>=2:
        if l[0]>l[1]:
            return('decrescente')
        elif l[0]<l[1]:
            return('crescente')
        else:
            return('nenhum')
    elif len(l)==1 or len(l)==0:
        print('nenhum')
    
    