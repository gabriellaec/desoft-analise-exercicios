def pos_arroba(email):
    for letra in email:
        if letra == "@":
            return email.index(letra)
        
def nome_usuario(email):
    return email[:pos_arroba(email)]