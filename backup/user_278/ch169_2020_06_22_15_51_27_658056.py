lista_i = []
login = input('Digite um login: ')
while login!='fim':
    lista_i.append(login)
    login = input('Digite um login: ')

lista_c = []
for i in lista_i:
    if i not in lista_c:
        lista_c.append(i)
    else:
        num = 1
        while i in lista_c:
            i2 = i+str(num)
            if i2 not in lista_c:
                lista_c.append(i2)
                break
            else:
                num+=1
for i in lista_c:
    print (i)