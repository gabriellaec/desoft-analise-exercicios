with open('texto.txt', 'r') as arquivo:
    ls=[]
    arq=arquivo.read()
    x=0
    ls=arq.split(' ')
    for i in ls:
        for n in range(len(i)):
            x+=1
    print(x)