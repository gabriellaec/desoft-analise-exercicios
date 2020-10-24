def eh_crescente(lista):
     
    if sorted(lista)==lista:
        return True
        
    elif lista==[] or len(lista)==1:
        return True
        
    elif lista[0]==lista[1]:
        return False
        
    else:
        return False
            
        