def login_disponivel(nome,lista):
    disponivel = False
    n=1
    while not disponivel:
        for nome_usado in lista:
            if nome == nome_usado:
                nome += n
                n+=1
                disponivel = False
                break
            else:
                disponivel = True
                
    return nome
            