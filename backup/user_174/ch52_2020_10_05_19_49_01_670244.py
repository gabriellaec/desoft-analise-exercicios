def calcula_total_da_nota(lista_1,lista_2):    
    i=0
    p=0
    
    while i<len(lista_1) and i<len(lista_2):
        p+=lista_1[i]*lista_2[i]
        i=i+1
    return (p)
        
    