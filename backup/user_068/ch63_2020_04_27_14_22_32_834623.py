def pos_arroba(str):
    a = str.find("@")
    return a
def nome_usuario(str):
    a = str[:pos_arroba(str)]
    return a