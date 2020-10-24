def pos_arroba(email):
    return(email.find('@'))

print(pos_arroba('leticiafs@al.insper.edu.br'))

def nome_usuario(email):
    pos = pos_arroba(email)
    return email[:pos]