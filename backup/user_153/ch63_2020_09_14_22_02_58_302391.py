def pos_arroba(email):
    for idx,c in enumerate(email):
        if c == '@':
            return idx

def nome_usuario(email):
    idx_arroba = pos_arroba(email)
    return email[:idx_arroba]
