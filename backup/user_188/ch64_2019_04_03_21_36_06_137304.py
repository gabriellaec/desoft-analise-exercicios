def pos_arroba(email):
    contador = 0
    while contador < len(email):
        if email[contador] == "@":
            return contador
        contador += 1

def nome_usuario(email):
    arroba = posicao_arroba(email)
    return email[:arroba]