
def inverte_lista(a):
    i = len(a)-1
    b = []
    while i < len(a):
        b.append(a[i])
        i -= 1
    if i < 0:
        break
    return b