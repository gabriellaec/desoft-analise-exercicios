
def login_disponivel(nome, lista):
    i=1
    if nome not in lista:
        return nome
    else:
        for x in range(len(lista)):
            while nome in lista:
                nome = nome +str(i)
                if nome in lista:
                    nome= nome[:-1]
                i+=1
            return nome
       
logins = []
nome = ''
while nome != 'fim':
    nome = input('nome: ')
    if nome != 'fim':
        login = login_disponivel(nome, logins)
        logins.append(login)
        print(login)