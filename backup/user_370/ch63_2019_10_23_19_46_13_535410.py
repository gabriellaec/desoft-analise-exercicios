def pos_arroba (email):
    n=len(email)
    i=0
    pos=-1
    
    while i < n:
        if email[i] == "@":
            pos+=1
            return(i)
        i+=1

    