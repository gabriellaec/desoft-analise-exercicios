def login_disponivel(txt, x):
    c = 0
    d = txt
    for i in range(len(x)):
        if d == x[i]:
            c += 1
            d = d[0:len(txt)] + str(c)
    return d

login = str(input('Qual o login? '))
z = []
while login != 'fim':
    login = str(input('Qual o login? '))
    z.append(login)
    confere = login_disponivel(login, z)
print('\n' confere)    
    
    
    