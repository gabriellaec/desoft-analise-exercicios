def login_disponivel(new, logins):
    if new not in logins:
        return new
    else:
        tem = True
        count = 1
        while tem:
            x = new + str(count)
            if x in logins:
                count += 1
            else:
                return x