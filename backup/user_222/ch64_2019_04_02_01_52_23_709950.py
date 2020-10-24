def pos_arroba(email):
    i=0
    while i<len(email):
        if email[i]=="@":
            return i
        i+=1
def nome_usuario(email):
    email2=pos_arroba(email)
    return email2[0:'@']