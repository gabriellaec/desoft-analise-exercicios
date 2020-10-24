with open('texto.txt','r') as arquivo:
    linhas=arquivo.readlines()
    y=' '.join(linhas)
    x=y.split(' ')
    print(len(x))