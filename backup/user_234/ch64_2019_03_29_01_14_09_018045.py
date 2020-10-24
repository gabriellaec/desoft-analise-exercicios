def pos_arroba(email):
    i=0
    tam_email=len(email)
    
    while i < tam_email:
        if email[i] == '@':
            return i
        i+=1
        
def nome_usuario(email):
    posit_arroba = pos_arroba(email)
    nome = email[:posit_arroba]
    return nome