def pos_arroba (email):
    n=len(email)
    i=0
    pos=-1
    
    while i < n:
        if email[i] == "@":
            pos+=1
            return(i)
        i+=1
def nome_usuario (email2):
    f=len(email2)
    k=0
    soma=0
    simbolo= "@"
    while k != f:
        if email2[k] == simbolo:
            soma+=1 
            return len(simbolo)
        k+=1
    t= email[:len(simbolo)]
    print (t)
        
            
        
        
            
        
            
     
    