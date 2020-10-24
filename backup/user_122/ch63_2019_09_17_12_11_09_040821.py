def pos_arroba(email):
    
    cont = 0
    for letra in email:
        if letra != "@":
            cont += 1
        else:
            break
            
    return cont