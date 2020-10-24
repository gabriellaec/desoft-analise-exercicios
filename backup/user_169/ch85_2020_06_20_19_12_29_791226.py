with open('macacos-me-mordam.txt','r') as arquivo:

    conteudo=arquivo.read()

    a=arquivo.split()

    lista=[]

    for i in a:
        if i.lower()=='banana':
           lista.append(i.lower())

            
    
    
            