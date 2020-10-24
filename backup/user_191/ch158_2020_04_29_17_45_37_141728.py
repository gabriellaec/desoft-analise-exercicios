with open('texto.txt','r') as arquivo:
    linhas=arquivo.readlines()
    x=linhas.split(' ')
    print(len(x))