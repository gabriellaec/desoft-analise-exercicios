with open('macacos-me-mordam.txt','r') as arquivo:
    i = 0
    while i < len(arquivo):
        if arquivo[i] == 'banana':
            print (arquivo[i])