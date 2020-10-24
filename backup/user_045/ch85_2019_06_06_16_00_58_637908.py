with open('macacos-me-mordam.txt','r') as arquivo:
    l = arquivo.read()
    c=0

    r=r.replace(' ',',')
    r=r.replace('/n',',')
    r=r.split(",")
    for e in r:
        g=e.lower()
        if g =='banana':
            c+=1
print(c)