def login_disponivel(login, lista_logins):
    # Se não existe o login...
    if login not in lista_logins:
        return login
    # Se já existe...
    else:
        i = 0
        contador = 1
        while i < len(lista_logins):
            # Verifica cada usuário na lista
            user = lista_logins[i]
            # Retira o número final dos logins correspondentes
            # e vai contando quantos tem para sugerir a próxima opção
            if user[:len(user)-1] == login:
                i += 1
                contador += 1
            i += 1
        contador = str(contador)
        return login + contador

logins = []
verifica = True
while verifica:
    new_user = input("Digite um nome de usuário: ")
    if new_user == 'fim':
        verifica = False
    else:
        if new_user not in logins:
            logins.append(new_user)
            print(new_user)
        else:
            new_user = login_disponivel(new_user, logins)
            logins.append(new_user)
            print(new_user)