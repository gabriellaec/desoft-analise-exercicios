with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo=arquivo.read()
    a=conteudo.split()
    x=0
    for i in a:
        if palavra.lower() =='banana':
            x+=1
            
    print(x)

            
    
    
            