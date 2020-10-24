def nome_usuario (texto):
    arroba = texto.find("@")
    nome = texto [:arroba]
    return nome