def ve_a(string):
    i = 0
    s = 0
    while i < len(string):
        if string[i] == 'a':
            s += 1
        i += 1
    return s

a = input("digite uma palavra: ")
