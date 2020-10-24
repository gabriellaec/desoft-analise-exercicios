def pos_arroba(e_mail):
    i=-1
    s='@'
    for a in e_mail:
       i+=1
       if a==s:
           return i
def nome_usuario(e_mail):
    q=pos_arroba(e_mail)
    usuario=e_mail[:q]
    return usuario
e_mail='asdf@asdf'
q=pos_arroba(e_mail)
w=nome_usuario(e_mail)