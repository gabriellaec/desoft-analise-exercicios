lista_nomes = []

x = input("Digite um nome para adicionar um login ou 'fim' para sair: ")
while x != 'fim':
    lista_nomes.append(x)
    x = input("Digite um nome para adicionar um login ou 'fim' para sair: ")

for i in lista_nomes:
    login = login_disponivel(i,logins)
    logins.append(login)
    print(login)