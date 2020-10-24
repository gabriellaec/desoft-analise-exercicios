def login_disponivel(txt, x):
    c = 0
    d = txt
    for i in range(len(x)):
        if d == x[i]:
            c += 1
            d = d[0:len(txt)] + str(c)
    return d

resposta = str(input('Qual o login? '))
z = []
while resposta != 'fim':
    z.append(login_disponivel(resposta, z))
    resposta = str(input('Qual o login? '))

for i in range(len(z)):
    print(z[i])   
   
    
    
    