with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo=arquivo.readlines()
    
    x=0
    for i in conteudo:
        if i.lower() =='banana':
            x+=1
            
    print(x)

            
    
    
            