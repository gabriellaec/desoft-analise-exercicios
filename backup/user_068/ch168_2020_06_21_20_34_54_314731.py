def login_disponivel(nome, lista):
    i=1
    if nome not in lista:
        return nome
    else:
        while nome in lista:
            
            nome = nome + str(i)
            
            i+=1
       