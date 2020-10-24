def login_disponivel (usuario, lista):
    i = 1
    login = usuario
    for nome in lista:
        if login == nome:
            login= usuario + str(i)
            i = i + 1
    return login

programa = True
lista_saida = []
while programa:
    logins = str(input('Digite um login'))
    if logins == 'fim':
        programa = False
    else:
        if not logins in lista_saida:
            lista_saida.append(logins)
        else:
            nome_atualizado = login_disponivel(logins, lista_saida)
            lista_saida.append(nome_atualizado)
            
if programa == False:
    print(lista_saida)