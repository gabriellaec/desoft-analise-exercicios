def login_disponivel(login,lista):
    i = 1
    while login in lista:
        login += str(i)
        if login in lista:
            login = login[:len(login)-1]
        i += 1
    return login

login = 'a'
lista = []
while login != 'fim':
    login = input("Entre com um login ou 'fim' para parar:\n>>>> ")
    if login != 'fim':
        lista.append(login_disponivel(login,lista))
for i in lista:
    print(i)