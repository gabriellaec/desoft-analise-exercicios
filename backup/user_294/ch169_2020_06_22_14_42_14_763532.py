lista_logins = []

 

login = input("Digite um login: ")
while not login == 'fim': 
    numero = 1
    login_inicial = login
    for string in lista_logins:
        if login == string:
            login = login_inicial
            login+=str(numero)
            numero+=1
            
    lista_logins.append(login)
    login = input("Digite um login: ")

 

for login in lista_logins:
    print(login)