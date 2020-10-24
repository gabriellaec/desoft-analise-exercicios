def classifica_lista(lista):
    a = len(lista)
    c = 0
    f = 0
    if a == 0:
        return 'nenhum'
    if a == 1:
        return 'nenhum'
    for i in range(a - 1):
        
        if c < a:
     
            if lista[i] < lista[i + 1]:
                
                C = True
                c += 1
            else:
                para = True
                c = a
                
    for i in range(a - 1):
        
        if f < a
            
            if lista[i] > lista[i + 1]:
                D = True
                f += 1
                
            else:
                D = False
                f = a
    if C:
        return "crescente"
    elif D:
        return "decrescente"
    else:
        return 'nenhum'
                
                
            
