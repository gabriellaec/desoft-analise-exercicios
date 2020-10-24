def login_disponivel(string,lista):
    v=1
    o=True
    while o:
            if string in lista:
                return string+f"{v}"
                v+=1
            else:
                return string
                o=False