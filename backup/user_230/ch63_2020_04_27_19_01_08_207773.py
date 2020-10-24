def nome_usuario (email):
    pos=email.find("@")
    usuario=email[:pos]
    return usuario