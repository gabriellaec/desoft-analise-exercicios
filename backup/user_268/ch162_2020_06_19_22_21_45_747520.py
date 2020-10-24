def verifica lista(lt):
    
    ch = []
    
    if len(lt) == 0: 
        return "misturado"
    
    for i in lt:
        if i%2==0:
            ch.append(i)
    if len(ch) == len(lt):
        return "par"
    
    elif len(ch) == 0:
        return "ímpar"
    
    else:
        return "misturado"
        
            
        
    
    