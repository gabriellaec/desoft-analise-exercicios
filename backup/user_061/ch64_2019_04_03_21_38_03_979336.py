def pos_arroba(email):
    i=0
    while i<len(email):
        if email[i]=="@":
            return i
        i+=1
        
def nome_usuario(email):
    return email[:pos_arroba(email)]