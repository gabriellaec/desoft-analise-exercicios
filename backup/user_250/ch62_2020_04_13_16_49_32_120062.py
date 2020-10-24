def pos_arroba(email):
    for letra in email:
        if letra == "@":
            return email.index(letra)