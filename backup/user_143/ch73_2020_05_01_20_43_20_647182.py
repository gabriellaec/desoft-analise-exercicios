def remove_vogais(s):
    li=['a', 'e', 'i', 'o', 'u']
    d=s
    for i in s:
        if i in li:
            d=s.replace(i, '')
            s=d
    return d
            