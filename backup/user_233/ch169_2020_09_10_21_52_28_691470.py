def login_disponivel(login, lista_logins):
    
    len_login = len(login)
    contagem = 0
    
    for login_usado in lista_logins:
        
        # BARRA NOMES DIFERENTES COM O NÚMERO DE CARACTÉRES MENOR OU IGUAL
        if login_usado[:len_login] != login:
            continue
        
        # CONTAGEM ESPECÍFICA PARA O PRIMEIRO NOME (nome sem número já existente)
        if len(login_usado) == len_login:
            contagem += 1
            continue
        
        # CONTAGEM PARA OS NOMES EXISTENTES
        try:
            int(login_usado[len_login])    # se for um número e não outra
            contagem += 1                  # letra, adicionar à contagem
            continue
        
        # BARRA NOMES COM O COMEÇO IGUAL
        except:
            continue
    
    if contagem == 0: return login
    
    return login + str(contagem)

logins = list()

while True:
    
    entrada = input()
    
    if entrada == 'fim': break
        
    logins.append(login_disponivel(entrada, logins))

for login in logins:
    print(login)



