
def login_disponivel(login, lista_logins):
    
    numero_max = 0
    
    for login_existente in lista_logins:
        if login_existente[:len(login)] == login:
            try:
                if int(login_existente[len(login)]) > numero_max: numero_max = int(login_existente[len(login)])
            except: continue
            
    
    if logins_iguais == 0: return login
    
    return login + str(numero_max + 1)
    

