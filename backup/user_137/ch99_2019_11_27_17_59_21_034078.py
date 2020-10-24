def login_disponivel(name, logins):
    n = name
    num = 1
    for i in range(len(logins)):
        if name == logins[i]:
            name = n + str(num)
            num += 1
            i = 0
    return name