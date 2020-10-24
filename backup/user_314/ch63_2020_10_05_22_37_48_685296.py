def pos_arroba(email):
    return email.find('@')

def nome_usuario (email):
    return email[0:pos_arroba(email)]