def pos_arroba(texto):
    i=0
    while i < len(texto):
        if texto[i] == '@':
            return i
        i+=1

def nome_usuario(texto):
    if pos_arroba(texto):
        return texto[0:texto[i]]