def pos_arroba(email):
    tamanho=len(email)
    i=0
    while i<tamanho:
        if email[i]=="@":
            return i
        i+=1
           
        