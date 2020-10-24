
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
    i=pos_arroba(email)
    s= nome_usuario(email2)
    print(s[:i])

        
        
            
        
            
     
    