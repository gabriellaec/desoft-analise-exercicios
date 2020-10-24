
def login_disponivel(login, lista_logins):
    
    len_login = len(login)
    contagem = 0
    
    for login_usado in lista_logins:
        
        try:
            if login_usado[:len_login] != login: continue
        
        except: continue
        
        try:
            int(login_usado[len_login])
            contagem += 1
        
        except: continue
    
    if contagem == 0: return login
    
    return login + str(contagem)
    

