def soma_valores(l):
    i = 0
    while l[i] <= l.last:
        s += l[i]
        i += 1
    if l[i] == False:
        Print(s)