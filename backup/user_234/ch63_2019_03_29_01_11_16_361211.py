def pos_arroba(email):
    i=0
    tam_email=len(email)
    
    while i < tam_email:
        if email[i] == '@':
            return i
        i+=1
        
def acha_nome(email):
    pos_arroba = acha_arroba(email)
    nome = email[:pos_arroba]
    return nome


print(acha_nome("juanruiz@gmail.com"))