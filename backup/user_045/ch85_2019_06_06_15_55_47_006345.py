with open('macacos-me-mordam.txt','r') as arquivo:
    l = arquivo.readlines()
    for r in l:
        r=r.replace(' ',',')
        r=r.replace('/n',',')
        r=r.split(",")
    c=0
    for i in l:
        for e in i:
            g=e.lower()
            if g =='banana':
                c+=1
print(3)