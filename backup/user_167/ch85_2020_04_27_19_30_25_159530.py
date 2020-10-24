with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    palavras=conteudo.split()
    
    cont=0
    for e in palavras:
        if e=='banana':
            cont+=1
    print(cont)
    
   
        
    

            