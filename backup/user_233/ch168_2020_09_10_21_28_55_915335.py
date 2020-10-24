
def login_disponivel(login, lista_logins):
    
    logins_iguais = 0
    
    for login_existente in lista_logins:
        if login_existente[:len(login)]: logins_iguais += 1
    
    if logins_iguais == 0: return login
    
    return login + str(logins_iguais)
    

