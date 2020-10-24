def pos_arroba (email):
    n=len(email)
    i=0
    pos=-1

    
    while i < n:
        if email[i] == "@":
            pos+=1
            return(i)
        i+=1

def nome_usuario (email):
    a=pos_arroba(email)
    bla=(email)[:a]
    return(bla)


nome = nome_usuario("dudatorres@gmail.com")
print(nome)    
    

        
            
        
            
     
    