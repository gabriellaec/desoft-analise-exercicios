def pos_arroba(email):
    for p,i in enumerate(email):
        if i == '@':    
            return p
print(pos_arroba('gabicuki@gmail.com'))


def nome_usuario(e):
    pos=pos_arroba(e)
    resp=e[:pos]
    return resp