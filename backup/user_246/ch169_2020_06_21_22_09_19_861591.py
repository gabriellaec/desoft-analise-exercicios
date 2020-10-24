def login_disponivel(nome, lista):
    if nome in lista:
        i=1
        login = ('{0}{1}'.format(nome,i))
        while login in lista:
            i+=1
            login = ('{0}{1}'.format(nome,i))
    else:
        login = nome        
    return login
user = input('Novo Usuario:')
novo = []
while user != 'fim':
    novo.append(login_disponivel(user))
    user = input('Novo Usuario:')
    
for i in novo:
    print(i)