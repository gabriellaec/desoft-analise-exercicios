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

semFim = True
logins = []
while semFim:
    log = input('Qual o login? ')
    if log == 'fim':
        semFim = False
    logins.append(log)

l_f = []
for i, l in enumerate(logins):
    print(login_disponivel(l, logins))
    