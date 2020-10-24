
def login_disponivel(login, lista_logins):
    
    numero = 0
    
    while True:
        
        if login not in lista_logins: return login
        
        numero += 1
        login += str(numero)
    

