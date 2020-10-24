def login_disponivel(login,lista_exist):
    continua=True
    #ve se ja existe na lista
    if login not in lista_exist:
        return login
    else:
        #vejo se ja tem um numero 
        #se sim
        if login[-1].isdigit():
            while continua:
                #vejo qual eh o numero
                x=int(login[-1])
                #adiciono um ao valor
                x+=1
                #tira o ultimo caractere(que no caso seria um numero)
                login=login[:-1]
                #adiciona o outro numero
                login+=str(x)
                if login not in lista:
                    continua=False
                else:
                    pass
            return login
        #se nao
        else:
            #adiciono 1
            login=login+'1'
            return login