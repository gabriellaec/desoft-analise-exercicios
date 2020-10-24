def nome_usuario(email):
    def pos_arroba(email):
        i=0
        while i<len(email):
            if email[i]=="@":
              return i 
            i=i+1
    arroba=pos_arroba(email)
    usuario=email[:arroba]
    return usuario

    