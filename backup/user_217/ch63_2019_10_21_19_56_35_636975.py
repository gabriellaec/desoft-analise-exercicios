def pos_arroba(email):
    
    
    contador=0
    
    for i in email:
        
        if i == '@':
            
            break
        contador+=1  
    return contador