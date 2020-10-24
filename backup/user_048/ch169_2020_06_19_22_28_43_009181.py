#registra logins
lista_logins=[]

#continua perguntando
pergunta=True
while pergunta:
    x=input('Qaul o login?')
    #ve se acabou
    #se sim para o loop
    if x=='fim':
        pergunta = False
    #se nao continua
    else:
        #e anota os valores 
        lista_logins.append(x)
print(lista_logins)
    
lista_veri=[]

def login_disponivel(login,lista_exist):
    continua=True
    #ve se ja existe na lista
    if login not in lista_exist:
        pass
    else:
        #so sei se nao estiver na lista e com numero
        while continua:
            #vejo se ja tem um numero 
            if login[-1].isdigit():
                    #vejo qual eh o numero
                    x=int(login[-1])
                    #adiciono um ao valor
                    x+=1
                    #tira o ultimo caractere(que no caso seria um numero)
                    login=login[:-1]
                    #adiciona o outro numero
                    login+=str(x)
                    #ve se ja esta na lista
            #ve se nao tem digito 
            else:
                #acrescenta um
                login+='1'
            if login not in lista_exist:
                continua=False
            else:
                pass
    lista_veri.append(login)
    return login
for nome in lista_logins:
    print(login_disponivel(nome,lista_veri))
