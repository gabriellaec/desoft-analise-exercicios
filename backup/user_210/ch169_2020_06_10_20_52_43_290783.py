def login_disponivel(login, lista_logins):
    cont = 1
    login_ok = login
    while login_ok in lista_logins:
        login_ok = login
        login_ok += str(cont)
        cont += 1
    return login

inp = input()
lista = []

while inp != "fim":
    lista.append(login_disponivel(inp, lista))
    inp = input()

for each in lista:
    print(each)
    