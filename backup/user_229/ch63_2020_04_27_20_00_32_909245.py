def pos_arroba(string):
    for i in range(len(string)):
        if string[i] == "@":
            return i

def nome_usuario(email):
    if pos_arroba(email):
        return email[0:pos_arroba(email)-1]