def login_disponivel(nome,lista):
    disponivel = False
    n=1
    novo_login=nome
    while not disponivel:
        for nome_usado in lista:
            if novo_login == nome_usado:
                novo_login = nome+str(n)
                n+=1
                disponivel = False
                break
            else:
                disponivel = True
                
    return nome
            