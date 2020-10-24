def login_disponivel(nome, lista):
    i=1
    if nome not in lista:
        return nome
    else:
        for name in range(len(lista)):
            while nome in lista: 
                nome = nome +str(i)
            return nome