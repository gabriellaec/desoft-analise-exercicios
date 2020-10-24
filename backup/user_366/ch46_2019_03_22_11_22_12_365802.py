def ve_a(string):
    i = 0
    s = 0
    while i < len(string):
        if string[i] == 'a':
            s += 1
        i += 1
    return s

a = input("digite uma palavra: ")
b = ve_a(a)
print("O A aparece {0} vezes nessa palavra". format(b))