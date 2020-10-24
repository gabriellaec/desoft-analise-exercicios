with open('macacos-me-mordam.txt', 'r') as arquivo:
    texto=arquivo.read()
    ts=texto.split()
    a=0
    for i in ts:
        i== i.lower()
        if i  =='banana':
            a+=1
     
    