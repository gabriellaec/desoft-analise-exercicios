def pos_arroba(email):
    email=[]
    i=0
    while i< len(email):
        if email[i] == @:
            return len(email[i])
        else:
            i+=1
            
        