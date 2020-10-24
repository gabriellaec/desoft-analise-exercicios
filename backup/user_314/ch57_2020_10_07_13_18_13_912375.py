def eh_PA(lista):
    
    if(len(lista)>1):

        r=lista[1]-lista[0]

        for i in range(len(lista)-1):
            
            if not (lista[i+1]-lista[i]==r):
                return False
        
        return True
    
    else:
        return True



def eh_PG(lista):
    if(len(lista)>1):
        
        if lista[0] == 0:
            return False
        q=lista[1]/lista[0]
            
        for i in range(len(lista)-1):
            if lista[i] == 0:
                return False
            elif not (lista[i+1]/lista[i] == q):
                return False
        
        return True

    else:
        return True

def verifica_progressao (lista): 
   
    if(eh_PG(lista)== True and eh_PA(lista)==True):
        return 'AG'
    elif(eh_PG(lista)== True):
        return 'PG'
    elif(eh_PA(lista)== True):
        return 'PA'
    else:
        return 'NA'
