lista_logins = []

pergunta_login = input('Digite um login: ')
while not pergunta_login == 'fim':

    nome_0 = pergunta_login
    numero = 0

    for login in lista:

        if pergunta_login == login:
            numero += 1
            pergunta_login = login + str(numero)
    
    if numero > 0:        
        login_final = nome_0 + str(numero)

    else: 
        login_final = nome_0

    lista_logins.append(login_final)

    pergunta_login = input('Digite um login: ')

for login in lista_logins:
    print(login)