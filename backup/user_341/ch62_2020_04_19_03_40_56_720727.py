def pos_arroba(email):
    x = 0
    for i in str(email):
        while i != "@":
            x = x + 1
        else:
            continue
    return x
    
            
           
        
            
        
