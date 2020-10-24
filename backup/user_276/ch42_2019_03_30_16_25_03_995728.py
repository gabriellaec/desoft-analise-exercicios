def quantos_uns(string):
    i = 0
    s = 0
    while i < len(string):
        if string[i] == 1:
            s += 1
        else:
            s = s
        i += 1
    return s
print(quantos_uns(str(1111)))