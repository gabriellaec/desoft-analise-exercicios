def calcula_total_da_nota(lista_1,lista_2):    
    i=0
    p=[]
    while i<len(lista_1) and i<len(lista_2):
        p.append((lista_1[i])*(lista_2[i]))
        i=i+1
    return (p)
        
    