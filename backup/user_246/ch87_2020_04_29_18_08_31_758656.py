with open('churras.txt','r') as c:
    linhas=c.readlines()
    x=0
    for i in linhas:
        s=i.split(',')
        x=x+(s[2])
    print(x)
    