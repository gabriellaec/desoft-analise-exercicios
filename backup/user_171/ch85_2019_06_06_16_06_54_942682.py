with open('macacos-me-mordam.txt', 'r') as arquivo:
    texto=arquivo.read()
    ts=texto.split()
    a=0
    for i in ts:
        if i.lower()  =='banana':
            a+=1
    print(a)
     
    