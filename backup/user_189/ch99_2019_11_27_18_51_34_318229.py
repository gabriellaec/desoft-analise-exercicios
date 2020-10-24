def login_disponivel(login):
    logins = ["jose","caludio","amelia"]
    letras = []
    for a in logins:
        if login == a:
            
            letras = list(login)
            log = ("".join(letras))
            letras.append("0")
        
            i = 0
            while log == a:
                letras[-1] = str(i)
                log = ("".join(letras))
                i += 1
            
            print(log)

a = str(input("insira seu login: "))  
print(login_disponivel(a))
