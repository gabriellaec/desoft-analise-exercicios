def login_disponivel(usuario,lista):
        if usuario not in lista:
            return usuario
        else:
            verifica=True
            i=1
            while verifica:
                novo=usuario+str(i)
                if novo not in lista:
                    verifica=False
                    return novo
                else:
                    i+=1
logins=[]
prog=True
while prog:
    usuario=input("Digite um login válido:")
    if usuario=="fim":
        prog=False
    else:
        login=login_disponivel(usuario,logins)
        logins.append(login)
for nome in logins:
    print (nome)
