def pos_arroba (email):
    n=len(email)
    i=0
    pos=-1
    
    while i < n:
        if email[i] == "@":
            pos+=1
            return(i)
        i+=1
    k=0
    simbolo= "@"
    while k != n:
        if email[k] == simbolo:
            k+=1
            return len(simbolo)
            t= email[:len(simbolo)]
            print (t)
        
            
        
        
            
        
            
     
    