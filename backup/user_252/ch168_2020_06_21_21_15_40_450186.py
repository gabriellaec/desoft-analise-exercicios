def login_disponivel(nome, lista):
    i=1
    if nome not in lista:
        return nome
    else:
        for nome in range(len(lista)):
            while nome in lista:
                nome = nome +str(i)
                if nome in lista:
                    nome= nome[:-1]
                i+=1
            return nome