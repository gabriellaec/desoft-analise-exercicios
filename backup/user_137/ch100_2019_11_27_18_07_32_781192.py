listaNomes = []
logins = []
while True:
    resp = input("Qual o nome do usuário desejado? ")
    if resp == 'fim':
        break
    a = login_disponivel(resp, logins)
    listaNomes.append(a)
    logins.append(a)

for n in listaNomes:
    print('\n' + n)