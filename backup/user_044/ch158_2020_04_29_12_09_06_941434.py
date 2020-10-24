with open('texto.txt', 'r') as arquivo:
    ls=[]
    x=0
    ls=arquivo.split()
    for i in ls:
        x+=len(i)
    print(x)