def verifica_numero(n):
    if n < 1:
        return False
    else:
        n = str(n)

        counter = 0
        i = 0
        while i < len(n):
            counter += int(n[i]) ** int(n[i])
            i += 1

        if int(n) == counter:
            return True
        else:
            return False