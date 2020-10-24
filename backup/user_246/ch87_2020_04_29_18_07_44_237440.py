with open('churras.txt','r') as c:
    linhas=c.readlines()
    for i in linhas:
        s=i.split(',')
        x=x+float(s[2])
    print(x)
    