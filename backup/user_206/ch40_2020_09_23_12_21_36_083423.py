def soma_valores(l):
    i = 0
    while l[i] <= l[-1]:
        s += l[i]
        i += 1
    if l[i] == l[-1]:
        Print(s)