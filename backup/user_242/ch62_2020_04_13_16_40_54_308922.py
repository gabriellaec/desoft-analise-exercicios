def pos_arroba(string):
    for arroba in string:
        if arroba == '@':
            return string.index(arroba)
