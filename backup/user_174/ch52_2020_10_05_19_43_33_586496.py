def calcula_total_da_nota(lista_1,lista_2):    
    i=0
    p=[]
    if len(lista_1)==0 or len(lista_2)==0:
        return ([0])
    while i<len(lista_1) and i<len(lista_2):
        p.append((lista_1[i])*(lista_2[i]))
        i=i+1
    return (p)
        
    