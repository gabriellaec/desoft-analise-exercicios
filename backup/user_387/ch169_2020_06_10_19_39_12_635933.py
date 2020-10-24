def login_disponivel(login,list):
    if login not in list:
        return login

    else:
        new_list = []
        for name in list:    
            for s in name:
                if s.isdigit():
                    test = name.replace(s,'')
                    if test == login: 
                        new_list.append(test)
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