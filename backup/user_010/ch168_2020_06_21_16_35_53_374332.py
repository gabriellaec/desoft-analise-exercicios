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