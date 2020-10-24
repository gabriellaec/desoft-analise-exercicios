def login_disponivel(login, lista_login):
    nome_login = login
    contador = 0
    x = True
    
    while x:
        if nome_login not in lista_login:
            return nome_login
            x = False
        else:
            contador += 1
            nome_login = login + str(contador)

lista_nomes = []
lista_nova = []
Y = True

while Y:
    nome = input('Digite um nome: ')
    if nome ==  'fim':
        Y = False
    else:
        lista_nomes.append(nome)
    
for nome in lista_nomes:
    lista_nova.append(login_disponivel(nome, lista_nova))

for i in lista_nova:
    print(i)

    
