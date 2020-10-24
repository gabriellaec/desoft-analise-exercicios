def pos_arroba (string):
    arroba = string.find("@")
    return arroba

def nome_usuario (texto):
    arroba = pos_arroba(string)
    nome = texto [:arroba]
    return nome