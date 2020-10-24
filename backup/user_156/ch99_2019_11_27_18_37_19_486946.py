def login_disponivel(nome, lista_logins):
    
    for i in len(lista_logins):
        if nome not in lista_logins:
            return nome
        elif nome in lista_logins:
            return nome[i]