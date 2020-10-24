def login_disponivel(nome, lista):
    if nome in lista:
        i=1
        login =str(i)join.nome[len(nome)+1]
        while login in lista:
            i+=1
            login = str(i)join.nome[len(nome)+1]
    else:
        login = nome
        
    return login