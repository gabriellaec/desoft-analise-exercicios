with open('macacos-me-mordam.txt','r') as arquivo:
    l = arquivo.readlines()
    c=0
    for r in l:
        r=r.replace(' ',',')
        r=r.replace('/n',',')
        r=r.split(",")
        for e in i:
            g=e.lower()
            if g =='banana':
                c+=1
   
print(c)