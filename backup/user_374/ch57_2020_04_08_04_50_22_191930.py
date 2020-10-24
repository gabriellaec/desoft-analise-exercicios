def verifica_progressao(lista):
    listar = lista
    pa = False
    na = False
    pg = False
    for i in range(0,len(lista)):
        if i >= 2:
            if listar[i] - listar[i-1] == listar[i-1] - listar[i-2]:
               pa = True
               na = False
               pg = False
           
            elif listar[i]/listar[i-1] == listar[i-1]/listar[i-2]:
                pg = True
                pa = False
                na = False
            
            else:
                pg = False
                pa = False
                na = True
                break
        elif i == 0:
            na = True
            pa = False
            pg = False
        
        elif len(listar) == 2:
            if listar[0] == 0:
               pa = True
               na = False
               pg = False
            elif listar[1]%listar[0] == 0 and listar[1] - listar[0] != 1:
               pa = False
               na = False
               pg = False
               return 'PA'
             
            else:
               pa = True
               na = False
               pg = False
        
        elif i >= 1:
            if lista[i] == lista[i-1]:
                return 'AG'
                
    if pa == True:
        return 'PA'
    elif pg == True:
        return 'PG'
    elif na == True:
        return 'NA'