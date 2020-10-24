def login_disponivel(login, indisponivel):
    if login not in indisponivel:
        return login
    
    else:
        quantidade = 0
        for utilizado in indisponivel:
            if utilizado[:len(login)] == login:
                quantidade+=1
        return login + '{}'.format(quantidade)

l = []
while True:
    s = input("Qual o usuário?")
    if s == "fim":
        break
    a = login_disponivel (s,l)
    l.append(a)

for i in l:
    print(i)