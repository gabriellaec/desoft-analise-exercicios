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
    z.append(lista_disponivel(z, login)
    login = str(input('Qual o login? '))

for i in range(len(z)):
    print(z[i])   
   
    
    
    