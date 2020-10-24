def login_disponivel(string,lista):
    v=1
    o=True
    while o:
            if string not in lista:
                return string
                o=False
            else:
                return string+f"{v}"
                v+=1
