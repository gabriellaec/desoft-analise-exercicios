def pos_arroba(email):
    i=0
    tamanho=len(email)
    while i<tamanho:
        i+=1
        if email[i]=="@":
            return i