with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    conteudo=conteudo.lower()
    a=0
    i=0
    cont=0
    lista_vazia=[]
    while i<len(conteudo):
        if conteudo[i]== ' ':
            lista_vazia.append(conteudo[:cont])
            cont=0
        i+=1
        cont+=1
    for d in lista_vazia:
        if d =='banana':
            a+=1
    print (a)
        