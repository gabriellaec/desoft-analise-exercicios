def nome_usuario (string):
    pos = string.find('@') 
    nome = string[:pos]
    return nome

