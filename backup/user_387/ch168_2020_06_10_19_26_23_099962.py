def login_disponivel(login,list):
    if login not in list:
        return login

    else:
        new_list = []
        for name in list:
            for s in name:
                if s.isdigit():
                    new_list.append(name.replace(s,''))
        return login + str(1 + len(new_list))