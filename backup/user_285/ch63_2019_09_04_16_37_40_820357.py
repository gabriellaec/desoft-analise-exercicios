def pos_arroba(email):
    cont=0
    for i in email: 
        if i == "@" :
            return cont
        cont = cont + 1