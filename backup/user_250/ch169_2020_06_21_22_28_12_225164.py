perguntar = True
listanomes = ['']
listalogins = []
while perguntar == True:
    entrada = input('Digite nome: ')
    if entrada == 'fim':
        perguntar = False
    else:    
        login = (login_disponivel(entrada, listanomes))
        listanomes.append(entrada)
        listalogins.append(login)

for i in listalogins:
    print(i)