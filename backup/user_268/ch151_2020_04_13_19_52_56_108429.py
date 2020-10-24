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
                
                CR = True
                c += 1
            else:
                CR = False
                c = a + 1
                
    for i in range(a - 1):
        
        if f < a:
            
            if lista[i] > lista[i + 1]:
                DR = True
                f += 1
                
            else:
                DR = False
                f = a + 1
    if CR:
        return "crescente"
    elif DR:
        return "decrescente"
    else:
        return 'nenhum'
                
                
            
