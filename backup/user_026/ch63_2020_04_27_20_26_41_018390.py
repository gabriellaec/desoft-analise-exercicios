def nome_usuario(texto):
    a= texto.find("@")
    nome= texto[:a]
    return nome
        