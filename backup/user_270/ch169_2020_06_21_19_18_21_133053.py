def login_disponivel(name,l):
    not_over = True
    if name not in l:
        return name
    else:
        i = 1
        while not_over:
            if name+str(i) not in l :
                not_over = False
            else:
                i+=1
        return name+str(i)


not_over = True
login = []
while not_over:
    name = input('Digite o seu login : /n')
    if name == 'fim' :
        not_over = False
    else:
        login.append(login_disponivel(name))
for i in login :
    print(i)
    
    