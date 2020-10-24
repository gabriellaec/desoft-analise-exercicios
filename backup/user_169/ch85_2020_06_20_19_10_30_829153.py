with open('macacos-me-mordam.txt','r') as arquivo:

    conteudo=arquivo.read()

    a=conteudo.split()

    for i in a:
        x = a.count('banana'.lower())

    print(x)


            
    
    
            