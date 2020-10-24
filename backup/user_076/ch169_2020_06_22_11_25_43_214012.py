nome = input("Digite seu login: ")
lista = []
while nome != 'fim':
    lista.append(nome)
    nome = input("Digite seu login: ")
    
def login_disponivel (login,lista):
    números = ['0','1','2','3','4','5','6','7','8','9']
    while login in lista:
        último_caracter = login[-1]
        if último_caracter not in números:
            login = login + "1"
        else:
            novo_digito = int(último_caracter) + 1
            login = login[:-1:] + str(novo_digito)
    return login

Lista=[]
for i in lista:
    novo_login = login_disponivel(i,Lista)
    Lista.append(novo_login)
    print(novo_login)