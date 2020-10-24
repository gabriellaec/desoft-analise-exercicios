def pos_arroba(email):
    i = 0
    while i <len(email):
        if email[i] == '@':
            a = i
            i+=1
        else:
            i+=1 
    return a

def nome_usuario(email):
    arroba = pos_arroba(email[a])
    return email[ :arroba]