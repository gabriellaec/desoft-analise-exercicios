def classifica_lista(lista):
    a = len(lista)
    para = False
    stop = False
    if a == 0:
        return 'nenhum'
    if a == 1:
        return 'nenhum'
    for i in range(a - 1):
        
        while not para:
     
            if lista[i] < lista[i + 1]:
                
                C = True
               
            else:
                para = True
                C = False
                
        while not stop:
            
            if lista[i] > lista[i + 1]:
                D = True
                
            else:
                D = False
                stop = True
    if C:
        return "crescente"
    elif D:
        return "decrescente"
    else:
        return 'nenhum'
                
                
            
