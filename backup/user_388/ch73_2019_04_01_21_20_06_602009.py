def remove_vogais(x):
    l = []
    for i in x:
        if i != 'a' or i !='o' or i != 'e' or i != 'i' or i != 'u':
            l.append(i)
    p = ''
    for i in l:
        p += i
    return p
            