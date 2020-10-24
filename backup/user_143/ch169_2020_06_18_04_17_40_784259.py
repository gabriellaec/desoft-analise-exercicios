def login_disponivel (n, l):
    c = 0
    num = 0
    for i in l:
        if n != i:
            c +=1
        elif n == i and num == 0:
            num += 1
            n = n + str(num)
        elif n == i and num >= 1:
            num += 1
            n = n.replace(str(num-1), str(num))
        
    if c == len(l):
        return n
    else:
        return n
lista = []
login = str(input('Usuário digita:'))
lista.append(login)
li = []
while login != 'fim':
    login = str(input('Usuário digita:'))
    lista.append(login)
    a = login_disponivel (login, lista)
    li.append(a)
for i in li:
    print(i)