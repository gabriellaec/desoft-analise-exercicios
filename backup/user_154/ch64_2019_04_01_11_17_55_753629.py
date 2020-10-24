def pos_arroba(string):
    return string.find("@")

def nome_usuario(string):
    return string[:pos_arroba(string)]