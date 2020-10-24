def pos_arroba(email):
    contador = 0
    for letra in email:
        if letra == '@':
            return contador
        contador += 1

def nome_usuario(email):
    return email[:pos_arroba(email)]