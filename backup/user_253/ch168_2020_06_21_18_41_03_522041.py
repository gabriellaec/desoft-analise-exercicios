def login_disponivel(nome, lista):
    i=0
    if nome not in lista:
        return nome
    else:
        for item in range(len(lista)):
            while nome in lista:
                i+=1
                nome = nome+ str(i)
                
        return nome