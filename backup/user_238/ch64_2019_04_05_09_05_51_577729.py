def nome_usuario(e):
    pos=pos_arroba(e)
    i=0
    resp='invalido'
    while i < len(e):
        if i==pos:
            resp=e[:pos]
        i+=1
        return resp