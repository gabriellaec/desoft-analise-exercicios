with open('texto.txt', 'r') as arquivo:
    ls=[]
    x=0
    sem_esp=arquivo.strip()
    ls=sem_esp.split()
    for i in ls:
        x+=len(i)
    print(x)