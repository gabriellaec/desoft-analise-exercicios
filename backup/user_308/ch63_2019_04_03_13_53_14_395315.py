def pos_arroba(email):
    contador=0
    pos=-1
    while contador<len(email):
        if email[contador]=="@":
        contador+=1
    return pos