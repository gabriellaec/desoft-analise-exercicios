def pos_arroba(email):
    contador = 0
    for letra in email:
        if letra == '@':
            return contador
        contador += 1
