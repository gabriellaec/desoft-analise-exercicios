def pos_arroba(string):
    for i in string:
        if i == '@':
            return string.index(i)