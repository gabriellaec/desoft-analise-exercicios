def login_disponivel(log, l):
    if log not in l:
        return log
    else:
        for i in range(len(l)):
            l[i] = l[i][:-1]
        repetiu = 1
        for nome in l:
            if nome == log:
                repetiu += 1
        return log + str(repetiu)

login = input('Qual o login? ')
l_logins = [login]

for login not 'fim':
    login = input('Qual o login? ')
    l_logins.append(login)

for i, l in enumerate(l_logins):
    l_logins[i] = login_disponivel(l, l_logins)
    print(l_logins[i])
