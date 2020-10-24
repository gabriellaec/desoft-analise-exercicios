def login_disponivel(nome, lista):
    i=1
    if nome not in lista:
        print(nome)
        return nome
    else:
        for name in range(len(lista)):
            while nome in lista:
                nome = nome +str(i)
                print(nome)
                if nome in lista:
                    nome= nome[:-1]
                    print(nome)
                i+=1
            return nome