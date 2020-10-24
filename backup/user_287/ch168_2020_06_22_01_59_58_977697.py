def login_disponivel(nome_login, lista_usuarios):
    nome_login = str(input('Insira seu login: '))
    lista_usuarios = ['andre', 'fabio', 'lucio']
    for i in range(100):        
        if nome_login in lista_usuarios:
            i += 1
            return nome_login + f'{i}
        else :
            return nome_login
        