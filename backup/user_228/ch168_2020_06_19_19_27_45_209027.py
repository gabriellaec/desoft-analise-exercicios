def login_disponivel(string,lista):
    v=1
    while v<100:
            if string in lista:
                return string+f"{v}"
                v+=1
            else:
                return string
                v+=1