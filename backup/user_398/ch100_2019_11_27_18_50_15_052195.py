def login_disponivel(login,lista_logins):
    if login not in lista_logins:
        return login
    else:
        n=0
        for e in lista_logins:
            if str(login) in str(e):
                n+=1                
        adicional=str(n)
        return str(login+adicional)
    
    

loop = True
lista=[]
while loop == True:
    login = str(input('Digite o login:'))
    if login == 'fim':
        break
    novo = login_disponivel(login,lista)
    lista.append(novo)
    
    
for e in lista:
    print('login:',e)
    