

def nome_usuario(texto):
    i=0
    while i < len(texto):
        if texto[i] == '@':
            return texto[0:i]
        