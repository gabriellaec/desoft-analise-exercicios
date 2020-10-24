lista_i = []
login = input('Digite um login: ')
while login!='fim':
    lista_i.append(login)
    login = input('Digite um login: ')
    if login == 'fim':
        break

def login_disponivel(lista_i):
    lista_c = []
    for i in lista_i:
        if i not in lista_c:
            lista_c.append(i)
        else:
            num = 1
            while True:
                if (i+str(num)) not in lista_c:
                    lista_c.append(i+str(num))
                    break
                else:
                    num+=1
    for i in lista_c:
        print (i)