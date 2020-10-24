def pos_arroba(email): 
    s=-1
    for w in email:
        s+=1
        if w == "@":
            s-1
            return s 
def nome_usuario(email):
    a=pos_arroba(email)
    return email[:a