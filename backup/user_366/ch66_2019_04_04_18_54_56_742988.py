def capitaliza(string):
    new = ''
    i = 0
    new += string[i].upper()
    i += 1
    while i < len(string):
        new += string[i]
        i += 1
    return new