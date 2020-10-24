def pos_arroba(email):
    cont= 0 
    for i in range(len(email)):
        if i == "@":
            cont=0
        else: 
            cont +=1
    return cont
          
        
    
       