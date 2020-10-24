with open('macacos-me-mordam.txt','r') as m:
    texto=m.read()
    s=texto.replace(A,a)
    s=s.replace(N,n)
    s=s.replace(B,b)
    s=s.split()
    x=0
    for i in s:
        if i=='banana':
            x+=1
    print(x)