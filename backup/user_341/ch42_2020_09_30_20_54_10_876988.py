l = []
palavra = input('palavra:')
while palavra != 'fim':
    l.append(palavra)
    palavra = input('palavra:')
i = 0
while i<len(l):
    if l[i][0] == 'a':
        print(l[i])
        i = i + 1
    else:
        i = i+1

