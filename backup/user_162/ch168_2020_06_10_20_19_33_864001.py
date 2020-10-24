def login_disponivel(n, lis):
    if n not in lis:
        return n
    else:
        lis1 = []
        for nome in lis:
            for c in nome:
                if c.isdigit():
                    new = nome.replace(c, "")
                    if new == n:
                        lis1.append(new)
    return n + str(1 + len(lis1)) 