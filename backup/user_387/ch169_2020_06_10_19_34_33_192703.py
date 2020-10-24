def login_disponivel(login,list):
    if login not in list:
        return login

    else:
        for name in list:
            new_list = []
            for s in name:
                if s.isdigit():
                    new_list.append(name.replace(s,''))
        return login + str(1 + len(new_list))

login = ''
list = []

while True:
    if login == 'fim':
        break
    login = input()
    list.append(login_disponivel(login,list))
list.remove('fim')
print(list)