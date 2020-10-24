def pos_arroba(x):
    
    i=0
    while i < len(x):
        if x[i]=="@":
            return i
        i+=1

def nome_usuario(email):
    pos = pos_arroba(email)
    return email[:pos]

        