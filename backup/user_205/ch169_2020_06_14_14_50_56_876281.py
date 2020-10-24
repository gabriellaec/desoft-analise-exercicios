def login_disponivel(login, lista):
    numero = 0
    #Se o login não está na lista, devolve sem alteração! 
    if login not in lista:
        return login
    #Login está na lista! 
    else:
        for logins in lista: 
            #Se o login for diferente, continua o loop
            if login != logins:
                continue
            #Login igual!
            else:
                numero +=1
                login_novo = login + str(numero)
                if login_novo not in lista:
                    return login_novo
                else:
                    while(login_novo in lista):
                        numero+=1
                        novo_login = login_novo.replace(login_novo[-1], str(numero))
                        if novo_login not in lista:
                            return novo_login 


lista = []
palavra = input("Digite o login: ")
while palavra != 'fim':
    filtro = login_disponivel(palavra, lista)
    lista.append(filtro)
    print("{0}".format(filtro))
    palavra = input("Digite o login: ")