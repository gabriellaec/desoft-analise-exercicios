with open('macacos-me-mordam.txt','r') as arquivo:
    a=arquivo.read()
    b=a.lower()
    c=b.split()
    x=0
    for i in c:
        if i== 'banana':
            x+=1
print (x)