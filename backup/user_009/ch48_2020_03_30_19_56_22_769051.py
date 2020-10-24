def eh_crescente(l):
    if len(l) <= 1:
        return False
    elif l == sorted(l):
        return True
        